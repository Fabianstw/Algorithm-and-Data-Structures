"""
Class Hashlist with linear probing
"""


class Hashlist:

    def __init__(self):
        self.size = 8
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

    def resize(self):
        pass

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
    hashlist.add_value(20, 2)
    hashlist.add_value(28, 2)
    print(hashlist.keys)
