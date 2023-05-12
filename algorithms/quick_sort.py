"""Module with implementation of the quick sort algo
"""
from typing import List
import random


def swap(i_one: int, i_two: int, arr: List[int]) -> None:
    """Method to swap two elements in the list
    """
    arr[i_one], arr[i_two] = arr[i_two], arr[i_one]


def quicksort(arr: List[int]) -> None:
    """In place sorting using quick sort method
    """
    quicksort_helper(arr, 0, len(arr)-1)
    return


def quicksort_helper(arr: List[int], left: int, right: int) -> None:
    """Helper to handle logic for quicksort
    """
    if left < right:
        pivot = left
        l, r = left, right
        while l < r:
            if arr[l] < arr[pivot]:
                l += 1
            elif arr[r] > arr[pivot]:
                r -= 1
            else:
                swap(l, r, arr)
        swap(pivot, r, arr)
        quicksort_helper(arr, left, r-1)
        quicksort_helper(arr, r+1, right)


if __name__=="__main__":
    arry = list(range(10))
    random.shuffle(arry)
    print(f"Before sort {arry}")
    quicksort(arr=arry)
    print(f"After sort {arry}")
