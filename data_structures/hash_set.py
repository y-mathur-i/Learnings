class HashList:
    def __init__(self):
        self.lst = []
    
    def update(self, key) -> None:
        if not self.find(key):
            self.lst.append(key)

    def find(self, key: int) -> bool:
        return any(x == key for x in self.lst)

    def remove(self, key) -> None:
        if self.find(key):
            self.lst.remove(key)

class HashSet:
    def __init__(self, key_size: int = 2096) -> None:
        self.key_size = key_size
        self.hash_set = [HashList() for _ in range(key_size)]
    
    def hash_value(self, key: int) -> int:
        return key%self.key_size
    
    def add(self, key: int) -> None:
        self.hash_set[self.hash_value(key)].update(key)
    
    def remove(self, key: int) -> None:
        self.hash_set[self.hash_value(key)].remove(key)

    def find(self, key) -> bool:
        return self.hash_set[self.hash_value(key)].find(key)

