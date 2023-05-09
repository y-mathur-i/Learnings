"""Module for bubble sort algo
"""
from typing import List
import random


def bubble_sort(arr: List[int]) -> None:
    """Method implementing bubble sort to sort the list in place"""
    while True:
        did_swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(i, i+1, arr)
                did_swap = True
        if not did_swap:
            return



def swap(idx_one: int, idx_two: int, arr: List[int]) -> None:
    arr[idx_one], arr[idx_two] = arr[idx_two], arr[idx_one]

if __name__=="__main__":
    arry = list(range(10))
    random.shuffle(arry)
    print(f"Before sort {arry}")
    bubble_sort(arr=arry)
    print(f"After sort {arry}")
