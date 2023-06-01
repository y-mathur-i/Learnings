"""Huffman encoding implementation
"""
from collections import Counter
from heapq import heappop, heapify, heappush
from dataclasses import dataclass


@dataclass
class Node:
    """Data class representing node in huffman tree
    """
    freq: int
    char: str = None
    left: object = None
    right: object = None

    def __lt__(self, other) -> bool:
        return self.freq < other.freq

        
def encode(string: str) -> None:
    """Method to encode string using huffman encoding
    """
    counter = Counter(string)
    # nodes = [Node(char=key, freq=value) for key, value in sorted(counter.items(), key=lambda x: x[0])]
    nodes = [Node(char=s, freq=string.count(s)) for s in set(string)]
    heapify(nodes)
    while len(nodes) > 1:
        left = heappop(nodes)
        right = heappop(nodes)
        print("left", left.char, left.freq)
        print("right", right.char, right.freq)
        new_node = Node(char="*", freq=left.freq+right.freq, left=left, right=right)
        heappush(nodes, new_node)
    mapping = {}
    get_mapping(node=nodes[0], mapping=mapping)
    print(mapping)

def get_mapping(node: Node, mapping: dict, curr_path: str = "") -> None:
    """Method to generate mapping from the huffman tree
    """
    if node is None:
        return
    if node.left is None and node.right is None:
        mapping[node.char] = curr_path
        return
    get_mapping(node.left, mapping, curr_path+"0")
    get_mapping(node.right, mapping, curr_path+"1")

if __name__=="__main__":
    STRING_TO_ENCODE = 'Huffman coding is a data compression algorithm.'
    STRING_TO_ENCODE = "A"*15 + "D"*6 + "C"*6  + "B"*7  + "E"*5
    encode(STRING_TO_ENCODE)
