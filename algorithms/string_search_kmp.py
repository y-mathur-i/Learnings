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
            arr[right] = left
            right += 1
        else:
            if left != 0:
                left = arr[left-1]
            else:
                arr[right] = 0
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
    lps_arr = create_lps_array(string=pattern)
    s_idx, p_idx  = 0, 0
    while s_idx < len(string_one):
        if string_one[s_idx] == pattern[p_idx]:
            s_idx, p_idx = s_idx + 1, p_idx + 1
        else:
            if p_idx != 0:
                p_idx = lps_arr[p_idx-1]  # at lps[s_idx-1] there is a proper prefix that is also a proper suffix
            s_idx += 1
        if p_idx == len(pattern):
            return s_idx - len(pattern)
    return -1


if __name__ == "__main__":
    assert search_string("absdcdsdcdcd", "cdcd") == 8
    assert search_string("abcd", "skjh") == -1
