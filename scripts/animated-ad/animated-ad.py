#!/usr/bin/env python3
"""Génère une publicité animée carrée à partir de l’agenda du MicroClub.

Dépendances Python : Pillow et PyYAML.
Exemples :
    python scripts/animated-ad/animated-ad.py
    python scripts/animated-ad/animated-ad.py --date 2026-11-13 --format mp4
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from textwrap import wrap

import yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[2]
AGENDA = ROOT / "data/agenda/agenda.yaml"
BACKGROUND = ROOT / "assets/images/site-background.webp"
CANVAS_SIZE = (1080, 1080)
OUTPUT_SIZE = (480, 480)
WARNING_SIZE = 6 * 1024 * 1024
MAX_SIZE = 16 * 1024 * 1024
FPS = 10
FRAME_COUNT = 90
MONTHS = [
    "JANVIER", "FÉVRIER", "MARS", "AVRIL", "MAI", "JUIN",
    "JUILLET", "AOÛT", "SEPTEMBRE", "OCTOBRE", "NOVEMBRE", "DÉCEMBRE",
]
WEEKDAYS = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Charge une police installée, avec un repli portable."""
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def clean(value: object) -> str:
    """Transforme le markdown/HTML de l’agenda en texte lisible."""
    text = "" if value is None else str(value)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<(https?://[^>\s]+)>", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    text = re.sub(r"[*_`~]", "", text)
    return html.unescape(text).strip()


def load_event(date_arg: str | None) -> tuple[dict, datetime]:
    data = yaml.safe_load(AGENDA.read_text(encoding="utf-8")) or {}
    events = data.get("events", [])
    parsed = []
    for event in events:
        try:
            when = datetime.fromisoformat(str(event["date"]))
        except (KeyError, ValueError):
            continue
        parsed.append((when, event))

    if date_arg:
        try:
            wanted = datetime.fromisoformat(date_arg)
        except ValueError as error:
            raise SystemExit(f"Date invalide : {date_arg!r} (attendu : YYYY-MM-DD)") from error
        matches = [(when, event) for when, event in parsed if when.date() == wanted.date()]
        if not matches:
            raise SystemExit(f"Aucun évènement trouvé à la date {date_arg}.")
        return min(matches, key=lambda item: item[0])

    now = datetime.now()
    future = [item for item in parsed if item[0] >= now and item[1].get("status") != "canceled"]
    if not future:
        raise SystemExit("Aucun évènement futur confirmé ou à confirmer n’a été trouvé.")
    return min(future, key=lambda item: item[0])


def background() -> Image.Image:
    image = Image.open(BACKGROUND).convert("RGB")
    scale = max(CANVAS_SIZE[0] / image.width, CANVAS_SIZE[1] / image.height)
    image = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = (image.width - CANVAS_SIZE[0]) // 2
    top = (image.height - CANVAS_SIZE[1]) // 2
    image = image.crop((left, top, left + CANVAS_SIZE[0], top + CANVAS_SIZE[1]))
    overlay = Image.new("RGBA", CANVAS_SIZE, (8, 12, 21, 105))
    image = Image.alpha_composite(image.convert("RGBA"), overlay)
    # Un léger assombrissement en bas améliore la lecture des liens et descriptions.
    shade = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shade)
    for y in range(400, CANVAS_SIZE[1]):
        alpha = round(175 * (y - 400) / (CANVAS_SIZE[1] - 400))
        draw.line((0, y, CANVAS_SIZE[0], y), fill=(4, 8, 14, alpha))
    return Image.alpha_composite(image, shade)


def draw_wrapped(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], *, width: int,
                 fnt: ImageFont.ImageFont, fill: tuple[int, int, int, int], spacing: int = 5) -> int:
    """Dessine un texte en lignes et retourne sa hauteur."""
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        words = paragraph.split()
        line = ""
        for word in words:
            candidate = f"{line} {word}".strip()
            if draw.textlength(candidate, font=fnt) <= width or not line:
                line = candidate
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
    draw.multiline_text(xy, "\n".join(lines), font=fnt, fill=fill, spacing=spacing)
    bbox = draw.multiline_textbbox(xy, "\n".join(lines), font=fnt, spacing=spacing)
    return bbox[3] - bbox[1]


def text_layer(event: dict, when: datetime, index: int) -> Image.Image:
    layer = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    white = (248, 249, 252, 255)
    muted = (211, 216, 228, 255)
    blue = (103, 178, 255, 255)
    violet = (190, 157, 255, 255)

    if index >= 0:
        draw.text((540, 48), "EPFL  •  LAUSANNE", font=font(25, True), fill=blue, anchor="ma")
        draw.text((72, 82), "MICROCLUB", font=font(88, True), fill=white)
        draw.text((76, 178), "Le club d’électronique et d’informatique", font=font(28), fill=muted)
    if index >= 1:
        draw.text((76, 318), "NOTRE PROCHAIN RENDEZ-VOUS", font=font(42, True), fill=white)
    if index >= 2:
        # Calendrier violet.
        box = (76, 430, 300, 654)
        draw.rounded_rectangle(box, radius=28, fill=(91, 38, 210, 245), outline=(130, 88, 255, 255), width=3)
        draw.text((188, 482), str(when.day), font=font(84, True), fill=white, anchor="ma")
        draw.text((188, 578), MONTHS[when.month - 1], font=font(25, True), fill=white, anchor="ma")
        draw.text((188, 620), str(when.year), font=font(25, True), fill=white, anchor="ma")

        date_text = f"{WEEKDAYS[when.weekday()]} {when.day} {MONTHS[when.month - 1].lower()} {when.year} À {when:%H:%M}"
        status = event.get("status", "confirmed")
        status_text = {"confirmed": "CONFIRMÉE", "tobeconfirmed": "À CONFIRMER", "canceled": "ANNULÉE"}.get(status, status.upper())
        draw.text((340, 435), date_text, font=font(21, True), fill=muted)
        badge_width = int(draw.textlength(status_text, font=font(18, True))) + 30
        draw.rounded_rectangle((350, 470, 350 + badge_width, 510), radius=20, outline=violet, width=2)
        draw.text((365, 479), status_text, font=font(18, True), fill=violet)
    if index >= 3:
        title = clean(event.get("title", ""))
        draw_wrapped(draw, title, (340, 535), width=650, fnt=font(31, True), fill=white, spacing=4)
    if index >= 4:
        speaker = clean(event.get("speaker", ""))
        if speaker:
            draw.text((340, 625), f"Présenté par {speaker}", font=font(24), fill=violet)
    if index >= 5:
        location = event.get("location") or {}
        location_name = clean(location.get("name", ""))
        if location_name:
            draw.text((340, 675), f"⌖  {location_name}", font=font(23, True), fill=blue)
    if index >= 6:
        description = clean(event.get("description", ""))
        notes = [clean(note) for note in (event.get("notes") or []) if clean(note)]
        links = [str(link) for link in (event.get("links") or []) if str(link).strip()]
        location = event.get("location") or {}
        location_url = str(location.get("url", "")).strip()
        if location_url:
            links.insert(0, location_url)
        footer_parts = [part for part in [description, *notes, "  ·  ".join(links)] if part]
        footer = "\n".join(footer_parts)
        if footer:
            draw_wrapped(draw, footer, (76, 735), width=928, fnt=font(20), fill=muted, spacing=5)
    return layer


def fade_in(layer: Image.Image, progress: float) -> Image.Image:
    progress = max(0.0, min(1.0, progress))
    alpha = layer.getchannel("A").point(lambda value: round(value * progress))
    result = layer.copy()
    result.putalpha(alpha)
    return result


def render_frames(event: dict, when: datetime) -> list[Image.Image]:
    base = background()
    layers = [text_layer(event, when, i) for i in range(7)]
    frames = []
    for frame_no in range(FRAME_COUNT):
        image = base.copy()
        elapsed = frame_no / FPS
        for index, layer in enumerate(layers):
            start = index * 0.75
            progress = (elapsed - start) / 0.45
            image = Image.alpha_composite(image, fade_in(layer, progress))
        frames.append(image.convert("RGB").resize(OUTPUT_SIZE, Image.Resampling.LANCZOS))
    return frames


def write_output(frames: list[Image.Image], output: Path, output_format: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output_format = output_format.lower()
    if output_format == "webp":
        frames[0].save(output, save_all=True, append_images=frames[1:], duration=1000 // FPS,
                       loop=0, format="WEBP", quality=90, method=6)
    elif output_format == "gif":
        frames[0].save(output, save_all=True, append_images=frames[1:], duration=1000 // FPS,
                       loop=0, format="GIF", optimize=False)
    elif output_format == "mp4":
        if not shutil.which("ffmpeg"):
            raise SystemExit("Le format MP4 nécessite ffmpeg, introuvable dans le PATH.")
        with tempfile.TemporaryDirectory(prefix="microclub-ad-") as temporary:
            directory = Path(temporary)
            for number, frame in enumerate(frames):
                frame.save(directory / f"frame-{number:04d}.png")
            command = ["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
                       "-i", str(directory / "frame-%04d.png"), "-c:v", "libx264",
                       "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output)]
            subprocess.run(command, check=True)
    else:
        raise SystemExit(f"Format non supporté : {output_format}")

    size = output.stat().st_size
    size_mib = size / (1024 * 1024)
    if size > MAX_SIZE:
        output.unlink(missing_ok=True)
        raise SystemExit(
            f"Fichier trop volumineux : {size_mib:.2f} Mo (limite : 16 Mo)."
        )
    if size > WARNING_SIZE:
        print(f"AVERTISSEMENT : fichier de {size_mib:.2f} Mo (cible recommandée : moins de 6 Mo).")
    else:
        print(f"Taille : {size_mib:.2f} Mo — OK")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="Date de l’évènement (YYYY-MM-DD). Par défaut : prochaine date.")
    parser.add_argument("--format", choices=("webp", "gif", "mp4"), default="webp",
                        help="Format de sortie (défaut : webp).")
    parser.add_argument("--output", type=Path, help="Fichier de sortie (déduit du format si omis).")
    args = parser.parse_args()

    event_date, event = load_event(args.date)
    output = args.output or (Path(__file__).parent / "out" / f"{event_date:%Y-%m-%d}-animated-ad.{args.format}")
    print(f"Évènement : {event_date:%Y-%m-%d %H:%M} — {clean(event.get('title', ''))}")
    print(f"Génération de {output}…")
    write_output(render_frames(event, event_date), output, args.format)
    print(f"Fichier créé : {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit("Interrompu.")
