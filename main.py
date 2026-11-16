"""List the Python task 02 exercise scripts."""

from pathlib import Path


def main():
    """Show the available scripts and how to run one."""
    source = Path(__file__).resolve().parent / "src"
    for script in sorted(source.glob("*.py")):
        print(f"python src/{script.name}")


if __name__ == "__main__":
    main()
