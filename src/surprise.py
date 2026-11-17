"""Replace a function's behavior with a surprise."""

from functools import wraps


def surprise(function):
    """Return a wrapper that prints 'surprise!' whenever it is called."""
    @wraps(function)
    def show_surprise(*_args, **_kwargs):
        print("surprise!")

    return show_surprise


if __name__ == "__main__":
    @surprise
    def greet(name):
        """Greet the given person."""
        print(f"Hello, {name}!")

    greet("Ada")
