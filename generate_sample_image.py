#!/usr/bin/env python3
"""
Generate a sample rendering of the base font.
"""

from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter

TEXT_COLOR = ImageColor.getrgb("black")
SAMPLE_TEXT = (
    "ABCDEFHI1234567890Oijl1IS5qt\"'$#!@{}[]()<>çéáÁÑÃÏ¡²³¤€¼½¾¥×÷ßø«»®␀␍␊"
    "␌▶⚓⯒✘✔✼✎␢…⌘⏎⌫⏻⏼➜●ЯЖ"
)
LINE_COLOR = ImageColor.getrgb("#88f")
TEXT_COLOR = ImageColor.getrgb("black")


def draw_sample():

    HEIGHT = 200
    WIDTH = 800
    background = Image.new("RGBA", (WIDTH, HEIGHT), ImageColor.getrgb("white"))
    foreground = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 0))
    draw_b = ImageDraw.Draw(background)
    draw_f = ImageDraw.Draw(foreground)
    label_font = ImageFont.truetype("./build/3270-Regular.ttf", size=15)

    y = 0
    for size in range(15, 55, 5):
        sample_font = ImageFont.truetype("./build/3270-Regular.ttf", size=size)
        offset = size * 0.7
        y += offset
        # Draw the background reference lines. Upper for the alpha ascender
        draw_b.line(((0, y + size * 0.2), (WIDTH, y + size * 0.2)), LINE_COLOR, 1)
        # Lower line for the baseline
        draw_b.line(((0, y + offset), (WIDTH, y + offset)), LINE_COLOR, 1)
        # Draw the point size we are using for the text.
        draw_f.text((0, y), str(size), TEXT_COLOR, font=label_font)
        # Draw the text itself
        draw_f.text((20, y), SAMPLE_TEXT, TEXT_COLOR, font=sample_font)

    img = Image.alpha_composite(background, foreground)

    img.save("build/3270_sample.png")

    return img


def draw_readability_test(blur_radius):
    sample_font = ImageFont.truetype("./build/3270-Regular.ttf", size=30)

    img = Image.new("RGB", (800, 35), ImageColor.getrgb("white"))
    draw = ImageDraw.Draw(img)
    draw.text(
        (40, 5),
        "bh 5S HX 6G AR kx gy Z2 Il 1l 1I OQ CG DO 0O",
        TEXT_COLOR,
        font=sample_font,
    )
    img = img.filter(ImageFilter.GaussianBlur(blur_radius))
    img.save(f"build/blur_{blur_radius}.png")
    return img


if __name__ == "__main__":
    sample = draw_sample()
    bands = []
    for radius in range(0, 6):
        rt = draw_readability_test(radius)
