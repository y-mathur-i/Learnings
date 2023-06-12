"""Module implementing prime number seieve
"""
from typing import List


def get_prime_numbers(n: int) -> List[int]:
    """Method to get prime numbers till n
    """
    numbers = [True for _ in range(n+1)]
    for idx in range(2, len(numbers)):
        if numbers[idx]:
            starting = idx*2
            for next in range(starting, len(numbers), idx):
                numbers[next] = False
    return [n for n in range(2, len(numbers)) if numbers[n]]


if __name__=="__main__":
    NUM_TILL_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert get_prime_numbers(100) == NUM_TILL_100
