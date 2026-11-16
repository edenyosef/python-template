"""Find files whose names start with 'deep'."""

from argparse import ArgumentParser
from pathlib import Path


def thats_the_way(directory):
    """Return the matching filenames in the given directory, sorted by name."""
    return sorted(
        entry.name
        for entry in Path(directory).iterdir()
        if entry.name.startswith("deep") and entry.is_file()
    )


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    print(thats_the_way(parser.parse_args().directory))
