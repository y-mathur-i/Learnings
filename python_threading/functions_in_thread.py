"""Module with examples of functions used as thread
"""
from threading import Thread
import time


def simple_fn() -> None:
    """Simple fn
    """
    print("Fn start")
    print("sleeping for 2 sec")
    time.sleep(2)
    print("Fn end with no args")


def fn_taking_args(name: str) -> None:
    """function that takes args
    """
    print(f"fn received argument: {name}")
    time.sleep(2)
    print(f"Fn executed with args")


if __name__=="__main__":
    simple_fn_thread = Thread(target=simple_fn)
    fn_with_args_thread = Thread(target=fn_taking_args, args=("yogesh",))  # args to be passed as a tuple
    fn_with_args_thread.start()
    simple_fn_thread.start()  # call function
    fn_with_args_thread.join()
    simple_fn_thread.join()  # wait for it to complete
