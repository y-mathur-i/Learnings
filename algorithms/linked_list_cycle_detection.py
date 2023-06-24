"""Implementation for cycle detection algoithm for a linked list
"""


class ListNode:
    """Linked List node
    """
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def has_cycle(node: ListNode) -> bool:
    """Method detects cycle with fast slow node method
    """
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False




if __name__=="__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    assert not has_cycle(node)
    last_node = ListNode(5)
    node.next.next.next.next = last_node
    last_node.next = node
    assert has_cycle(node)
