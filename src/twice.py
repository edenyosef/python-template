"""Run a decorated function twice."""

from decorator import decorator


@decorator
def twice(function, *args, **kwargs):
    """Call the function twice and return the result of the second call."""
    function(*args, **kwargs)
    return function(*args, **kwargs)


if __name__ == "__main__":
    @twice
    def greet(name):
        """Greet the given person."""
        print(f"Hello, {name}!")

    greet("Ada")
