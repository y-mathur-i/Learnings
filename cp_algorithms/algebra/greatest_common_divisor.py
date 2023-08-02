"""GCD implementation recursive
    GCD can also be used to evaluate LCM the formulae is LCM(a,b) = a.b/gcd(a, b)
"""


def get_gcd(a: int, b: int):
    """EH
    """
    if b == 0:
        return a
    return get_gcd(b, a%b)


if __name__=="__main__":
    assert get_gcd(20, 12) == 4
