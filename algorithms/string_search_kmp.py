"""Module with kmp algorithm for string searching
"""


def search_string(string_one: str, string_two: str) -> int:
    """Method to search for string_two in string_one
        usign kmp algorithm and return the first index it shows up on.
    """ 
    assert len(string_one) >= len(string_two)
    # my understanding
    # 1. we for each point in s1 know the lenght of the longest proper prefix for s2
    # that ends there.



if __name__ == "__main__":
    string_one = "aaaaaabcb"
    string_two = "aaaaabc"
    print(search_string(string_one, string_two))
 