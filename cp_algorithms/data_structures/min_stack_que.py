"""Stack in which we find the minimum of inserted elements in o(1)
"""
from collections import deque


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


class MinQueueOne:
    """The main idea is:
        1. Remove from tail smaller elements than the one to be inserted
        2. When popping from front only pop in case the element in the one we want to pop
        --> index data is lost
    """
    def __init__(self) -> None:
        self.que = deque()

    def get_min(self) -> int:
        """Get minumum from inserted elements
        """
        return self.que[0] if self.que else None

    def push(self, val: int) -> None:
        """push element into the queue
        """
        while self.que and self.que[0] > val:
            self.que.pop()
        self.que.append(val)

    def remove_element(self, val: int) -> None:
        """Remove from ele based ont the val
        """
        while self.que and self.que[0] == val:
            self.que.popleft()




