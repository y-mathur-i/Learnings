"""Kadanes algo
"""
from typing import List


def max_sub_array_sum(arr: List[int]) -> int:
    """Fn returns max sum possible for a subarray
    """
    curr_sum = arr[0]
    res = arr[0]
    for num in arr[1:]:
        # choose to start a new sum or add curr element to the sum
        curr_sum = max(curr_sum+num, num)
        res = max(res, curr_sum)
    return res


if __name__=="__main__":
    lis_ = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_sub_array_sum(lis_) == 6
