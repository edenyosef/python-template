"""Measure how long a function call takes."""

from time import perf_counter


def running_2000(function, /, *args, **kwargs):
    """Call the function once and return its elapsed time in seconds."""
    start = perf_counter()
    function(*args, **kwargs)
    return perf_counter() - start


timer = running_2000


if __name__ == "__main__":
    print(running_2000(sorted, [3, 1, 2], reverse=True))
