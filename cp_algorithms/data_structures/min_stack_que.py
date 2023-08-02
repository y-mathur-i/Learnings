"""Stack in which we find the minimum of inserted elements in o(1)
"""


class MinStack:
    """Idea is to store a pair <int, int>
        and the second of the pair represents the minimum this far
        While still allowing us to perform conventional stack operations
        with same time complexity
    """
    def __init__(self) -> None:
        self.stk = []

    def push(self, val: int) -> None:
        """Push to stack
        """
        self.stk.append((val, min(self.stk[-1][-1], val)))

    def pop(self) -> None:
        """pop from stack
        """
        if self.stk:
            ele = self.stk.pop()
            print("element popped ", ele[0])
            print("Min element ", ele[1])
            return
        print("stk if empty")
