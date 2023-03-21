"""
Example of a decorator in python
"""
from typing import Callable


def my_decorator(function: Callable) -> Callable:
    """
    Example decorator
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
