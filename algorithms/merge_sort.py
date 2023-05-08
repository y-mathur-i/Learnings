"""Module with merge sort implementation
"""
from typing import List
import random


def merge_sort(arr: List[int]) -> List[int]:
    """Merge sort implementation
    """
    if len(arr) >= 2:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        i = j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
    return arr


if __name__=="__main__":
    arry = list(range(10))
    random.shuffle(arry)
    print(f"Before sort {arry}")
    merge_sort(arr=arry)
    print(f"After sort {arry}")
