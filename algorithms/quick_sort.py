"""Module with implementation of the quick sort algo
"""
from typing import List



def swap(i_one: int, i_two: int, arr: List[int]) -> None:
    """Method to swap two elements in the list
    """
    arr[i_one], arr[i_two] = arr[i_two], arr[i_one]
