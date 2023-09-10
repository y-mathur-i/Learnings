"""
Convert the string to a number so we can easily compare them
Point to remember the hashing algo has limited set of keys and there will be clashes
"""


def calc_hash(string: str) -> str:
    """Method to calc hash of a given string
        The idea being for a string for length n
        with chars c0, c1, c2, c3...., cn
        so it will  c0 + c1*p, c2*p^2, c3*p^3.... cn*p^(n-1) mod m
        where p is a prime number
        usually p is no of char for small case 31 works well
        and if small and large both 53 works
    """
    p = 31
    hsh = 0
    MOD = 10**9 + 7
    i = 0
    p_pow = 1
    while i < len(string):
        curr_char = string[i]
        curr_char_val = ord(curr_char)
        hsh += (curr_char_val*p_pow)%MOD
        p_pow *= p
        i += 1
    return hsh


if __name__=="__main__":
    print(calc_hash("yhososoos") == calc_hash("yhososoos"))
    print(calc_hash("yhososoos") == calc_hash("okokokoko"))
