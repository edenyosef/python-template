"""Create decorators that validate the type of a single argument."""

from functools import wraps
from inspect import signature


class ArgumentTypeError(TypeError):
    """A decorated function received an argument of the wrong type."""


def type_check(expected_type):
    """Return a decorator that validates arguments with isinstance."""
    def decorate(function):
        function_signature = signature(function)

        @wraps(function)
        def checked(*args, **kwargs):
            bound = function_signature.bind(*args, **kwargs)
            bound.apply_defaults()
            name, value = next(iter(bound.arguments.items()))
            if not isinstance(value, expected_type):
                raise ArgumentTypeError(
                    f"{name} must be {expected_type.__name__}, "
                    f"got {type(value).__name__}."
                )
            return function(*args, **kwargs)

        return checked

    return decorate


if __name__ == "__main__":
    @type_check(int)
    def double(number):
        """Double an integer."""
        return number * 2

    print(double(3))
