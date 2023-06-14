"""Implementation of a stack
"""


class Stack:
    """Stack implementation
    """
    def __init__(self, size) -> None:
        self.size = size
        self.stk = [None for _ in range(size)]
        self.curr_size = -1
    
    def push(self, val: int) -> bool:
        """Push val to stack
        """
        if self.curr_size + 1 < self.size:
            self.curr_size += 1
            self.stk[self.curr_size] = val
            return True
        return False

    def pop(self) -> int:
        """Pop value from stack
        """
        if self.curr_size - 1 >= -1:
            elem = self.stk[self.curr_size]
            self.curr_size -= 1
            return elem
        raise IndexError


if __name__=="__main__":
    stk = Stack(5)
    for n in range(5):
        stk.push(n)
    for _ in range(5):
        print(stk.pop())
