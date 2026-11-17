"""Group iterable items by the result of a key function."""

from collections import defaultdict


def group_by(function, iterable):
    """Return a dictionary of lists, preserving item order within each group."""
    groups = defaultdict(list)
    for item in iterable:
        groups[function(item)].append(item)
    return dict(groups)


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
