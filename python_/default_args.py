"""Example of how default arguments are bad
"""


def add_to_list(arr = []):
    """Method with mutable default args
    """
    arr.append("First")
    print(arr)



if __name__=="__main__":
    add_to_list()
    add_to_list()  # will print the list ["First", "First"]
