"""Read a secret message encoded as one black pixel per image column."""

from argparse import ArgumentParser
from pathlib import Path

from PIL import Image

# The course PNG encodes its black pixels with an RGB value of (1, 1, 1).
BLACK_PIXELS = {(0, 0, 0), (1, 1, 1)}


def remember_remember(image_path):
    """Decode black-pixel row indices as characters, from left to right."""
    with Image.open(image_path) as source:
        image = source.convert("RGB")

    pixels = image.load()
    message = []
    for column in range(image.width):
        black_rows = [
            row for row in range(image.height) if pixels[column, row] in BLACK_PIXELS
        ]
        if len(black_rows) != 1:
            raise ValueError(f"Column {column} must contain exactly one black pixel.")
        message.append(chr(black_rows[0]))
    return "".join(message)


def main():
    """Decode the supplied image or the example from the course."""
    parser = ArgumentParser(description=__doc__)
    default_image = Path(__file__).with_name("resources") / "code.png"
    parser.add_argument("path", nargs="?", type=Path, default=default_image)
    print(remember_remember(parser.parse_args().path))


if __name__ == "__main__":
    main()
