"""Module for insertion sort
"""
from typing import List
import random


def swap(i: int, j: int, arr) -> None:
    arr[i], arr[j] = arr[j], arr[i]



def insertion_sort(arr: List[int]) -> None:
    """Method finds the smallest element and swaps it with the the no as position
    1 to n (1 indexed)
    """
    for a_start in range(len(arr)-1):
        min_ele_idx = a_start
        for a_end in range(a_start+1, len(arr)):
            min_ele_idx = min(min_ele_idx, a_end, key=lambda x: arr[x])
        if min_ele_idx != a_start:
            swap(min_ele_idx, a_start, arr)
    return


if __name__=="__main__":
    arry = list(range(10))
    random.shuffle(arry)
    print(f"Before sort {arry}")
    insertion_sort(arr=arry)
    print(f"After sort {arry}")
