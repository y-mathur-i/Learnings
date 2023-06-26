"""Module with implementing generators in python
"""


def sq_numbers(nums) -> int:
    """Method returns a generator for squaring the numbers
    """
    for i in nums:
        yield i*i  # to generator


sq_nums = sq_numbers([1, 2, 3, 4, 5])  # This returns a generator object

print(next(sq_nums))  # 1
print(next(sq_nums))  # 4
print(next(sq_nums))  # 9
print(next(sq_nums))  # 16
print(next(sq_nums))  # 25
# print(next(sq_nums))  # will throw an iteration error

# can loop over the generator
for num in sq_numbers([1, 2, 3, 4, 5]):
    print(num)

# generator saves space as the whole list is not generated and stored in memory

## can convert a list comprehension to generator by replacing [] with ()
nums_ = [x*x for x in [1, 2, 3, 4, 5]] # -> [(*x for x in [1, 2, 3, 4, 5])

# performance
