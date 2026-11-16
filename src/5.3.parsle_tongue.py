"""Extract secret messages embedded in a binary file."""

from argparse import ArgumentParser
from pathlib import Path

CHUNK_SIZE = 4096
MINIMUM_LETTERS = 5
LOWERCASE_ASCII = range(ord("a"), ord("z") + 1)
EXCLAMATION_MARK = ord("!")


def parsle_tongue(file_path):
    """Yield lowercase ASCII runs of at least five letters ending in '!'."""
    letters = bytearray()
    with open(file_path, "rb") as source:
        chunk = source.read(CHUNK_SIZE)
        while chunk:
            for byte in chunk:
                if byte in LOWERCASE_ASCII:
                    letters.append(byte)
                    continue

                if byte == EXCLAMATION_MARK and len(letters) >= MINIMUM_LETTERS:
                    yield letters.decode("ascii") + "!"
                letters.clear()
            chunk = source.read(CHUNK_SIZE)


def main():
    """Print each message from the supplied file or the course logo."""
    parser = ArgumentParser(description=__doc__)
    default_logo = Path(__file__).with_name("resources") / "logo.jpg"
    parser.add_argument("path", nargs="?", type=Path, default=default_logo)
    for message in parsle_tongue(parser.parse_args().path):
        print(message)


if __name__ == "__main__":
    main()
