"""
Example of a decorator in python
"""
from typing import Callable


def my_decorator(function: Callable) -> Callable:
    """
    Example decorator
    One caveat is that on calling help .i.e the function data like and and doc
    It will return the wrapper functions doc and name for a wrapped function
    To handle that (The logic works without it to)
    we use something called @wraps from functools
    """
    def wrapper(*args, **kwargs):  # to allow passing of arguments to the function it wraps
        """
        Function returned on calling the decorator.
        """
        return_value = function(*args, **kwargs)  # if i want the fucntion to return
        # can now log this value or perform operations
        return return_value
    return wrapper


@my_decorator
def hello_world(name):
    """Function being wrapped"""
    print(f"hello {name}")


def main() -> None:
    """Main method"""
    hello_world("Yogesh")


if __name__ == "__main__":
    main()
