"""Majority voting algorithm
"""
from typing import List


def find_element_with_max_freq(arr: List[int]) -> int:
    """Method to find element with highest freq in array
    using boyer moore algo
    """
    ele_count = 0
    curr_ = None
    for n in arr:
        if curr_ != n:
            if ele_count:
                ele_count -= 1
            else:
                ele_count = 1
                curr_ = n
        else:
            ele_count += 1
    count = 0
    for n in arr:
        if n == curr_:
            count += 1
    return n if count >= len(arr)//2 else -1


if __name__=="__main__":
    lst = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
    print(find_element_with_max_freq(lst))