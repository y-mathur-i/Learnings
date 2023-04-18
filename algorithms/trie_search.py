"""Module with implementation for trie data structure
"""


class TrieSearch:
    """Class implementing trie data structure
    """
    def __init__(self) -> None:
        self.root = {}
    
    def insert(self, word: str) -> None:
        """Method will iterate over the letter of the word
        and insert them one by one
        """
        curr_node = self.root
        for l in word:
            if l not in curr_node:
                curr_node[l] = {}
            curr_node = curr_node[l]
        curr_node["*"] = True

    def search(self, word: str) -> bool:
        """Method to search for the word by checking for each letter
        """
        curr_node = self.root
        for l in word:
            if l not in curr_node:
                return False
            curr_node = curr_node[l]
        return "*" in curr_node

if __name__ == "__main__":
    trie = TrieSearch()
    trie.insert("HELLO")
    assert trie.search("HELLO")
    assert not trie.search("BYE")

