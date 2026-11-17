"""Join lists with a separator between adjacent lists."""


def cup_of_join(*lists, sep="-"):
    """Return a new list, or None if no lists were supplied."""
    if not lists:
        return None

    joined = list(lists[0])
    for items in lists[1:]:
        joined.append(sep)
        joined.extend(items)
    return joined


join = cup_of_join


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))
