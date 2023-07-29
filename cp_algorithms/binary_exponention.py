"""Example implementation fo binary exponention
"""


def binary_expo(n: int, x: int) -> int:
    """Raise n to power of x
    """
    res = 1
    while x:
        if x&1:
            res = res*n
        n *= n
        x >>= 1
    return res



if __name__=="__main__":
    assert binary_expo(3, 13) == pow(3, 13)
