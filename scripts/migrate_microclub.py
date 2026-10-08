#!/usr/bin/env python3
"""Convertit une copie HTTrack de microclub.ch en contenus Hugo."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup


def quoted(value: str) -> str:
    return json.dumps(html.unescape(value), ensure_ascii=False)


def load_index(directory: Path) -> dict[int, dict]:
    return {
        int(path.stem): json.loads(path.read_text(encoding="utf-8"))
        for path in directory.glob("*.json")
    }


def clean_url(value: str, base_url: str) -> str:
    if not value or value.startswith(("#", "data:", "mailto:", "tel:", "javascript:")):
        return value
    absolute = urljoin(base_url, value)
    parsed = urlparse(absolute)
    if parsed.netloc not in ("microclub.ch", "www.microclub.ch"):
        return value
    path = unquote(parsed.path)
    if path.startswith("/wp-content/uploads/"):
        path = "/media/" + path.removeprefix("/wp-content/uploads/")
    path = re.sub(r"/index\.html$", "/", path)
    suffix = f"?{parsed.query}" if parsed.query else ""
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""
    return path + suffix + fragment


def clean_content(rendered: str, base_url: str) -> tuple[str, set[str]]:
    soup = BeautifulSoup(rendered, "html.parser")
    media: set[str] = set()
    for unwanted in soup.select("script, style, form"):
        unwanted.decompose()
    for tag in soup.find_all(True):
        for attr in ("style", "id", "loading", "decoding"):
            tag.attrs.pop(attr, None)
        if "class" in tag.attrs:
            tag.attrs.pop("class", None)
        for attr in ("src", "href", "poster"):
            if attr in tag.attrs:
                tag[attr] = clean_url(str(tag[attr]), base_url)
                if str(tag[attr]).startswith("/media/"):
                    media.add(str(tag[attr]).split("?", 1)[0])
        # Les variantes WordPress sont souvent absentes de la copie. Le fichier
        # principal reste responsive grâce au CSS, sans srcset cassé.
        tag.attrs.pop("srcset", None)
        tag.attrs.pop("sizes", None)
    return str(soup).strip(), media


def comments_from_html(path: Path) -> tuple[str, int]:
    if not path.exists():
        return "", 0
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="replace"), "html.parser")
    blocks: list[str] = []
    for article in soup.select("ul.comment-list article.comment"):
        author = article.select_one(".comment-author .fn")
        date = article.select_one(".comment-date-time")
        body = article.select_one(".comment-content")
        if not body:
            continue
        for link in body.select(".comment-reply-login"):
            link.decompose()
        li = article.find_parent("li", class_=lambda c: c and "comment" in c)
        depth = 1
        if li:
            for cls in li.get("class", []):
                if cls.startswith("depth-") and cls[6:].isdigit():
                    depth = int(cls[6:])
        prefix = "↳ Réponse — " if depth > 1 else ""
        name = author.get_text(" ", strip=True) if author else "Anonyme"
        when = date.get_text(" ", strip=True) if date else "Date inconnue"
        blocks.append(f"### {prefix}{name} — {when}\n\n{str(body).strip()}")
    if not blocks:
        return "", 0
    return "\n\n".join(blocks), len(blocks)


def find_local_media(mirror: Path, public_path: str) -> Path | None:
    relative = public_path.removeprefix("/media/")
    candidate = mirror / "wp-content" / "uploads" / relative
    if candidate.exists():
        return candidate
    # HTTrack suffixe certains téléchargements différés (p.ex. .cf.delayed).
    delayed = sorted(candidate.parent.glob(candidate.stem + ".*.delayed"))
    if delayed:
        return delayed[0]
    stem = candidate.with_suffix("")
    for extension in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".pdf", ".zip"):
        alternative = stem.with_suffix(extension)
        if alternative.exists():
            return alternative
    # Certains noms reçoivent un hash HTTrack juste avant l'extension.
    hashed = sorted(candidate.parent.glob(candidate.stem + "*" + candidate.suffix))
    if hashed:
        return hashed[0]
    # En dernier recours, réutilise une autre taille WordPress de la même image.
    base = re.sub(r"-\d+x\d+$", "", candidate.stem)
    variants = sorted(candidate.parent.glob(base + "*"))
    for variant in variants:
        if variant.is_file() and variant.suffix.lower() not in (".html", ".htm"):
            return variant
    return None


def write_front_matter(data: dict) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            rendered = ", ".join(quoted(str(item)) for item in value)
            lines.append(f"{key}: [{rendered}]")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, int):
            lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {quoted(str(value))}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mirror", type=Path, help="Répertoire microclub.ch de la copie HTTrack")
    parser.add_argument("destination", type=Path, help="Racine du projet Hugo")
    args = parser.parse_args()
    mirror = args.mirror.resolve()
    destination = args.destination.resolve()
    api = mirror / "wp-json" / "wp" / "v2"
    posts = load_index(api / "posts")
    pages = load_index(api / "pages")
    users = load_index(api / "users")
    categories = load_index(api / "categories")
    destination.mkdir(parents=True, exist_ok=True)
    all_media: set[str] = set()
    comment_total = 0

    for post in posts.values():
        date = post["date"]
        year, month, day = date[:10].split("-")
        slug = post["slug"]
        base_url = post["link"]
        body, media = clean_content(post["content"]["rendered"], base_url)
        all_media.update(media)
        html_path = mirror / year / month / day / slug / "index.html"
        comments, count = comments_from_html(html_path)
        comment_total += count
        author = users.get(post.get("author", 0), {}).get("name", "Auteur inconnu")
        category_names = [categories[c]["name"] for c in post.get("categories", []) if c in categories]
        tag_slugs: list[str] = []
        if html_path.exists():
            article = BeautifulSoup(html_path.read_text(errors="replace"), "html.parser").select_one("article")
            if article:
                tag_slugs = [c.removeprefix("tag-") for c in article.get("class", []) if c.startswith("tag-")]
        front = {
            "title": post["title"]["rendered"],
            "date": date,
            "lastmod": post.get("modified", date),
            "author": author,
            "categories": category_names,
            "tags": tag_slugs,
            "url": f"/{year}/{month}/{day}/{slug}/",
            "wordpress_id": post["id"],
            "comment_count": count,
        }
        output = destination / "content" / "articles" / year / month / day / f"{slug}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        comments_section = "\n\n## Commentaires\n\n"
        if comments:
            comments_section += comments + "\n\n"
        comments_section += "<!-- Ajoutez un commentaire ci-dessous sous la forme : ### Votre nom — AAAA-MM-JJ -->\n"
        output.write_text(write_front_matter(front) + body + comments_section, encoding="utf-8")

    page_order = {"historique": 10, "agenda": 20, "photos": 30, "liens": 40, "contacts": 50, "forum": 60}
    for page in pages.values():
        slug = page["slug"]
        if slug == "login":
            continue
        body, media = clean_content(page["content"]["rendered"], page["link"])
        all_media.update(media)
        front = {
            "title": page["title"]["rendered"],
            "date": page["date"],
            "lastmod": page.get("modified", page["date"]),
            "url": f"/{slug}/",
            "weight": page_order.get(slug, 100),
        }
        output = destination / "content" / "pages" / f"{slug}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(write_front_matter(front) + body + "\n", encoding="utf-8")

    missing: list[str] = []
    for public_path in sorted(all_media):
        source = find_local_media(mirror, public_path)
        if not source:
            missing.append(public_path)
            continue
        target = destination / "static" / public_path.removeprefix("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    report = {
        "articles": len(posts),
        "pages": len(pages) - 1,
        "comments": comment_total,
        "media_references": len(all_media),
        "missing_media": missing,
    }
    (destination / "migration-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
