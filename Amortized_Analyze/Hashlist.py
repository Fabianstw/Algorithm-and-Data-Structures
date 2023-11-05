"""
Class Hashlist with linear probing
"""
import random


class Hashlist:

    def __init__(self):
        self.size = 4
        self.count = 0
        self.values = [None] * self.size
        self.keys = [None] * self.size

    def hash(self, k):
        return k % self.size

    def find_value(self, key):
        hash_value = self.hash(key)
        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                return self.values[hash_value]
            hash_value += 1
        return None

    def add_value(self, key, value):
        if self.find_value(key) is not None:
            return "Key-Error: Key already used"
        hash_value = self.hash(key)
        while self.keys[hash_value] is not None:
            hash_value += 1
        self.keys[hash_value] = key
        self.values[hash_value] = value
        self.count += 1
        if self.count >= self.size // 4:
            self.resize()

    def resize(self):
        self.size *= 2
        new_keys = [None] * self.size
        new_values = [None] * self.size

        for index in range(len(self.keys)):
            if self.keys[index] is not None:
                hash_value = self.hash(self.keys[index])
                while new_values[hash_value] is not None:
                    hash_value += 1
                new_keys[hash_value] = self.keys[index]
                new_values[hash_value] = self.values[index]
        self.keys = new_keys
        self.values = new_values

    def remove_key(self, key):
        """
        Not programmed cause not necessary for the task
        :param key:
        :return:
        """
        pass


if __name__ == '__main__':
    hashlist = Hashlist()
    hashlist.add_value(12, 2)
    hashlist.add_value(22, 2)
    print(hashlist.keys)
    hashlist.add_value(28, 2)
    for i in range(80):
        hashlist.add_value(random.randint(0, 1000), 2)
    print(hashlist.keys)
