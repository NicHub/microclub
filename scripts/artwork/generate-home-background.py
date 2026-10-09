#!/usr/bin/env python3
"""Create the original Microclub night-sky artwork (no external photographs).

Requires Python 3, numpy, Pillow, cairosvg and the system Cairo library.
From the repository root:
    python3 scripts/artwork/generate-home-background.py

The fixed seed keeps the stars, nebulae and electronic constellations reproducible.
The foreground is editable in radiosonde.svg; both WebP crops are generated here.
"""

from io import BytesIO
from pathlib import Path
from xml.etree import ElementTree

import cairosvg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[2]
ARTWORK = Path(__file__).with_name("radiosonde.svg")
OUTPUT = ROOT / "assets" / "images"


def noise_field(width, height, rng):
    field = np.zeros((height, width), dtype=np.float32)
    weights = (1.0, 0.58, 0.31, 0.16, 0.085, 0.045)
    for cells, weight in zip((8, 18, 40, 85, 180, 380), weights):
        grid = rng.random((cells, max(2, int(cells * width / height)))).astype(
            np.float32
        )
        layer = Image.fromarray(grid).resize((width, height), Image.Resampling.BICUBIC)
        field += np.asarray(layer) * weight
    return np.clip(field / sum(weights), 0, 1)


def galaxy_axis(u, portrait):
    if portrait:
        return 0.72 - 0.54 * u + 0.05 * np.sin(7 * u)
    return 0.78 - 0.64 * u + 0.055 * np.sin(6.5 * u)


def sky(width, height, rng, portrait):
    u = np.linspace(0, 1, width, dtype=np.float32)[None, :]
    v = np.linspace(0, 1, height, dtype=np.float32)[:, None]
    clouds = noise_field(width, height, rng)
    filaments = noise_field(width, height, rng)
    axis = galaxy_axis(u, portrait)
    warp = (filaments - 0.5) * 0.16
    band = np.exp(-((v - axis + warp) / 0.105) ** 2)
    mist = np.exp(-((v - axis) / 0.23) ** 2)
    dust_lane = np.exp(-((v - axis + 0.015 + warp * 0.42) / 0.025) ** 2)
    cloudlight = band * np.clip((clouds - 0.20) * 1.75, 0, 1) ** 2
    cloudlight *= 1 - 0.83 * dust_lane
    # A quiet, near-black area sits behind the homepage title and introduction.
    quiet = 1 - 0.82 * np.exp(-((u - 0.48) / 0.25) ** 2 - ((v - 0.35) / 0.22) ** 2)
    vignette = np.clip(1 - 0.38 * ((u - 0.5) ** 2 + (v - 0.48) ** 2), 0.4, 1)
    rgb = np.empty((height, width, 3), dtype=np.float32)
    warm = np.exp(-((u - 0.16) / 0.28) ** 2)
    for channel, (base, glow, haze, amber) in enumerate(
        ((2.5, 83, 7, 20), (3.3, 80, 8, 9), (5.0, 105, 12, 0))
    ):
        rgb[:, :, channel] = (
            base + cloudlight * (glow + warm * amber) + mist * haze * clouds
        ) * quiet * vignette
    grain = rng.normal(0, 0.6, (height, width)).astype(np.float32)
    rgb += grain[:, :, None]
    return Image.fromarray(np.uint8(np.clip(rgb, 0, 255)))


def stars(image, rng, portrait):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    halos = Image.new("RGBA", image.size)
    halo_draw = ImageDraw.Draw(halos)
    palette = ((157, 176, 197), (205, 208, 211), (192, 180, 164), (171, 168, 201))

    def star(x, y, radius, brightness, halo=False):
        color = np.array(palette[int(rng.integers(len(palette)))])
        quiet = 1 - 0.72 * np.exp(
            -((x / width - 0.48) / 0.25) ** 2 - ((y / height - 0.35) / 0.22) ** 2
        )
        color = tuple(np.uint8(color * brightness * quiet))
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
        if halo:
            size = radius * 5
            halo_draw.ellipse(
                (x - size, y - size, x + size, y + size), fill=(*color, 23)
            )
            draw.line((x - size, y, x + size, y), fill=tuple(c // 3 for c in color))
            draw.line((x, y - size, x, y + size), fill=tuple(c // 3 for c in color))

    count = 3100 if portrait else 6900
    for _ in range(count):
        x, y = rng.uniform(0, width), rng.uniform(0, height)
        star(x, y, rng.uniform(0.25, 0.9), rng.uniform(0.12, 0.45))
    for _ in range(count):
        u = rng.uniform(-0.08, 1.08)
        y = (galaxy_axis(u, portrait) + rng.normal(0, 0.070)) * height
        if 0 < y < height:
            star(u * width, y, rng.uniform(0.22, 0.7), rng.uniform(0.09, 0.36))
    for _ in range(60 if portrait else 125):
        x, y = rng.uniform(0, width), rng.uniform(0, height * 0.83)
        star(x, y, rng.uniform(0.9, 1.65), rng.uniform(0.5, 0.85), halo=True)
    return Image.alpha_composite(image.convert("RGBA"), halos.filter(ImageFilter.GaussianBlur(3)))


def electronic_constellations(image, portrait):
    width, height = image.size
    layer = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(layer)
    scale = width / 3200 if not portrait else width / 1600

    def trace(points):
        points = [(x * width, y * height) for x, y in points]
        draw.line(points, fill=(119, 163, 181, 33), width=max(1, round(scale)))
        for x, y in (points[0], points[-1]):
            r = 2.7 * scale
            draw.ellipse((x - r, y - r, x + r, y + r), outline=(150, 181, 197, 83))
            draw.ellipse((x - 0.8, y - 0.8, x + 0.8, y + 0.8), fill=(204, 222, 228, 116))

    # Real PCB-style 45-degree traces read first as faint stellar filaments.
    trace(((0.025, 0.68), (0.085, 0.68), (0.125, 0.61), (0.175, 0.61)))
    trace(((0.055, 0.73), (0.125, 0.73), (0.165, 0.66), (0.21, 0.66)))
    trace(((0.11, 0.55), (0.15, 0.55), (0.19, 0.62), (0.24, 0.62)))
    trace(((0.24, 0.54), (0.27, 0.54), (0.31, 0.47), (0.37, 0.47)))
    trace(((0.66, 0.19), (0.70, 0.19), (0.74, 0.12), (0.81, 0.12)))
    trace(((0.70, 0.24), (0.75, 0.24), (0.79, 0.17), (0.84, 0.17)))
    trace(((0.86, 0.085), (0.90, 0.085), (0.935, 0.145), (0.99, 0.145)))
    # A miniature microcontroller hidden among the lower-left constellations.
    cx, cy = width * 0.205, height * (0.625 if not portrait else 0.70)
    size = 57 * scale
    draw.rounded_rectangle(
        (cx - size / 2, cy - size / 2, cx + size / 2, cy + size / 2),
        radius=5 * scale,
        outline=(134, 158, 184, 37),
        width=max(1, round(scale)),
    )
    for i in range(6):
        offset = (i - 2.5) * size / 8
        for sign in (-1, 1):
            draw.line(
                (cx + offset, cy + sign * size / 2, cx + offset, cy + sign * size * 0.75),
                fill=(134, 158, 184, 39),
                width=max(1, round(scale)),
            )
            draw.line(
                (cx + sign * size / 2, cy + offset, cx + sign * size * 0.75, cy + offset),
                fill=(134, 158, 184, 39),
                width=max(1, round(scale)),
            )
    return Image.alpha_composite(image, layer)


def earth(image, rng, portrait):
    width, height = image.size
    x = np.arange(width, dtype=np.float32)[None, :]
    y = np.arange(height, dtype=np.float32)[:, None]
    radius = width * (3.4 if portrait else 1.60)
    cx = width * 0.30
    cy = radius + height * (0.88 if portrait else 0.80)
    distance = np.sqrt((x - cx) ** 2 + (y - cy) ** 2) - radius
    surface = distance < 0
    texture = noise_field(width, height, rng)
    pixels = np.array(image.convert("RGB"), dtype=np.float32)
    for channel, (base, cloud, rim) in enumerate(((2, 2, 35), (5, 3, 62), (8, 5, 82))):
        pixels[:, :, channel] = np.where(
            surface, base + texture * cloud, pixels[:, :, channel]
        )
        pixels[:, :, channel] += (
            np.exp(-(distance / (height * 0.006)) ** 2) * rim
            + np.exp(-(distance / (height * 0.026)) ** 2) * rim * 0.12
        )
    image = Image.fromarray(np.uint8(np.clip(pixels, 0, 255))).convert("RGBA")
    # Remote, barely visible settlements establish the enormous difference in scale.
    lights = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(lights)
    for _ in range(650 if not portrait else 160):
        px = rng.normal(width * 0.20, width * 0.14)
        py = rng.normal(height * 0.96, height * 0.035)
        ix, iy = int(px), int(py)
        if 0 <= ix < width and 0 <= iy < height and distance[iy, ix] < -20:
            alpha = int(rng.uniform(25, 100))
            draw.point((ix, iy), fill=(163, 133, 87, alpha))
    return Image.alpha_composite(image, lights)


def foreground(image, portrait):
    width, height = image.size
    if portrait:
        art_width, left, top = int(width * 0.45), int(width * 0.58), int(height * 0.11)
    else:
        art_width, left, top = int(width * 0.31), int(width * 0.64), int(height * 0.07)
    artwork = ElementTree.parse(ARTWORK).getroot()
    if portrait:
        # A longer suspension puts the electronics below the introductory text
        # on narrow screens, without moving the balloon into the heading.
        artwork.find(".//*[@id='payload']").set(
            "transform", "translate(429 1178) rotate(-13 100 120)"
        )
        artwork.find(".//*[@id='suspension']").set(
            "d", "M558 650 C539 800 570 1020 532 1177"
        )
    png = cairosvg.svg2png(bytestring=ElementTree.tostring(artwork), output_width=art_width)
    sonde = Image.open(BytesIO(png)).convert("RGBA")
    image.alpha_composite(sonde, (left, top))
    return image


def generate(width, height, portrait=False):
    rng = np.random.default_rng(1976)
    image = sky(width, height, rng, portrait)
    image = stars(image, rng, portrait)
    image = electronic_constellations(image, portrait)
    image = earth(image, rng, portrait)
    image = foreground(image, portrait)
    name = "microclub-stratosphere-mobile.webp" if portrait else "microclub-stratosphere.webp"
    path = OUTPUT / name
    image.convert("RGB").save(path, "WEBP", quality=88, method=6)
    print(f"{path.relative_to(ROOT)}: {width} × {height}, {path.stat().st_size // 1024} KiB")


if __name__ == "__main__":
    generate(3200, 1800)
    generate(1000, 1640, portrait=True)
