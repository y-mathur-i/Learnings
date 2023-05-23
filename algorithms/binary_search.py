"""Module implementing binary search
"""
from typing import List


def binary_search(arr: List[int], key: int) -> int:
    """Method returns index if element found in array
        using binary search
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right+left)//2
        if arr[mid] > key:
            right = mid -1
        elif arr[mid] < key:
            left = mid + 1
        else:
            print("here")
            arr[mid]
            return mid
    return -1


if __name__=="__main__":
    arr = list(range(10))
    print(binary_search(arr, 5))
