"""
The idea is 
"""
from typing import List


def get_sieve(n: int) -> List:
    """
    sieve of erastoshenes
    """
    nos = [True]*(n+1)
    for i in range(2, len(nos)):
        if nos[i]:
            for j in range(i*2, len(nos), i):
                nos[j] = False
    return [i for i in range(len(nos)) if nos[i]]


if __name__=="__main__":
    print(get_sieve(100))
