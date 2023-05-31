"""Module with singly linked list implementation
"""


class ListNode:
    """List node 
    """
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    """Singly linked list
    """
    def __init__(self) -> None:
        self.head = None

    def add(self, val: int) -> None:
        """add node with value to list
        """
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
    
    def search(self, val: int) -> bool:
        """Search for node with value in linked list
        """
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def print_list(self) -> None:
        """Method to print the list
        """
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__=="__main__":
    linked_list = SinglyLinkedList()
    for n in range(5):
        linked_list.add(n)
    linked_list.print_list()
