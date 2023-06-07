"""Module with implementation of counting sort algorithm
"""
from typing import List


def count_sort(array: List[int]) -> List[int]:
    """Method for counting sort
    """
    # table to be used for counting
    min_ele = min(array)
    max_ele = max(array)
    freq_table = [0]*(max_ele-min_ele + 1)
    for num in array:
        freq_table[num-min_ele] += 1

    # convert freq table to starting index table
    total = 0
    for idx, freq in enumerate(freq_table):
        old = freq
        freq_table[idx] = total
        total += old

    res = [None for _ in range(len(array))]

    for n in array:
        res[freq_table[n-min_ele]] = n
        freq_table[n-min_ele] += 1

    return res


if __name__=="__main__":
    A = [4, 2, 10, 10, 1, 4, 2, 1, 10]
    print(count_sort(A))