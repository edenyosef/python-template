"""Interleave iterables in round-robin order, lazily or as a list."""

from collections import deque


def generator_interleaves(first, *others):
    """Yield one item per iterable in turn until every iterable is exhausted."""
    active = deque(map(iter, (first, *others)))
    while active:
        current = active.popleft()
        try:
            item = next(current)
        except StopIteration:
            continue
        active.append(current)
        yield item


def interleaves(first, *others):
    """Return the interleaved items as a list."""
    return list(generator_interleaves(first, *others))


interleave = interleaves


if __name__ == "__main__":
    print(interleaves("abc", [1, 2, 3], ("!", "@", "#")))
    print(list(generator_interleaves([1, 2], [3])))
