"""Used to answer range queries min/max
   Can only be used in case the data doesn't change between queries though
   Idea is -> any n can be represented as sum of numbers of power of 2
   13 -> 8 + 4 + 1
   Same way range can also be for example
   [2, 14] -> [2, 9] U [10, 13] U [14, 14]

   So, we pre compute the query for all the ranges
   The range combination function SHOULD be associative
    Overlap friendly function -> Allows o(1) answers
    No what is that ?

    Example: let f(x, y) = x + y
    there are three ranges
    r1, r2, r3 [we computed their sum]
    f(f(r1, r2), f(r2, r3)) != f(r1, f(r2, r3))

    
    Array

    [0, -1, 2, 4, 5, 10, 12, -34, 12, 3, 1, 8, 4, 7, 8]

    
    To start we need 
"""
from typing import List
import math


def construct_sparse_table(arr: List[int], computation_fn: callable) -> List:
    """Create sparse table
        it is of form
        [   ] 1st level
        [   ] 2nd level
        [   ] max possible level .i.e max power of 2 that is less than len of array
        each level is of size n
        Each cell represent answer for function in range [j, j + 2^i)
        We ignore all the partial ranges
    """
    res = []
    size = len(arr)
    levels = math.floor(math.log2(size))
    res = [[0]*size for _ in range(levels+1)]
    res[0] = arr[:]
    for i in range(1, len(res)):
        for j in range(len(res[i])):
            if j + (1 << (i-1)) < len(res[i]):
                res[i][j] = computation_fn(res[i-1][j], res[i-1][j + (1 << (i-1))])
    for row in res:
        print(row)
    return res


if __name__ == "__main__":
    array = [4,2,3,7,1,5,3,3,9,6,7,-1,4]
    construct_sparse_table(array, computation_fn=min)
