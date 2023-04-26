"""Module with kmp algorithm for string searching
"""
from typing import List


def create_lps_array(string: str) -> List[int]:
    """Method to generate lps array
    """
    arr = [0]*len(string)
    right, left = 1, 0
    while right < len(string):
        if string[left] == string[right]:
            left += 1
        else:
            left = 0
        arr[right] = left
        right += 1
    return arr

def search_string(string_one: str, pattern: str) -> int:
    """Method to search for string_two in string_one
        usign kmp algorithm and return the first index it shows up on.
        proper prefix & proper suffix
        prefix and sufix that are subset of the string
        longest proper prefix that is also a sufix
        so we prepare a lps array where for each i we know a preffix that is also a suffux

    """
    assert len(string_one) >= len(pattern)
    lps_arr = create_lps_array(string=string_one)
    s_idx, p_idx  = 0, 0
    while s_idx < len(string_one):
        if string_one[s_idx] == pattern[p_idx]:
            s_idx, p_idx = s_idx + 1, p_idx + 1
        else:
            if p_idx != 0:
                p_idx = lps_arr[s_idx-1]
            s_idx += 1
        if p_idx == len(pattern):
            return p_idx - len(pattern)
    return -1


if __name__ == "__main__":
    assert search_string("abcd", "ab") == 0
    assert search_string("abcd", "skjh") == -1
