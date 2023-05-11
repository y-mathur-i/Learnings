"""Module with sample implementation for the bloom filter
   Which is a probabilistic data structure
"""
import math
import mmh3
from typing import List


class BloomFilter:
    """Bloom filter class
    """
    def __init__(self, filter_size: int, no_hash: int) -> None:
        self.size = size
        self._no_hash_fn = no_hash
        self._n = 0
        self._filter = [0 for _ in range(size)]

    def reset_filter(self) -> None:
        """Method to clear out the filter
        """
        self._filter = [0 for _ in range(self.size)]

    def get_hash_indexes(self, key: str) -> List[int]:
        """Method to pass the key through the hash function and
            get the indexes
        """
        return [(hash(key) + i * mmh3.hash(key)) % self.size
                for i in range(1, self._no_hash_fn + 1)]

    def search(self, key: str) -> bool:
        """Method to check if the key exists .i.e was visited again
        """
        for i in self.get_hash_indexes(key):
            if not self._filter[i]:
                return False
        return True

    def add(self, key: str) -> None:
        """Method to add key to bloom filter
        """
        for i in self.get_hash_indexes(key):
            self._filter[i] = 1
        self._n += 1

if __name__=="__main__":
    size = 10
    no_hash_functions = 5
    bloom_filter = BloomFilter(filter_size=size, no_hash=no_hash_functions)
    bloom_filter.add("key")
    print(bloom_filter.search("key"))
    print(bloom_filter.search("okp"))