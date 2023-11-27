"""Abgabe Blatt 1 Teil d"""


class BitVektoren:

    def __init__(self):
        self.dynamic_set = 0b110
        self.size = 3

    def has(self, a):
        if a > self.size:
            return False
        else:
            copy_of_set = self.dynamic_set
            copy_of_set >>= a
            has_value = copy_of_set ^ ((copy_of_set >> 1) << 1)
            if has_value == 1:
                return True
        return False

    def insert(self, a):
        if a > self.size:
            self.size = a + 1
            self.dynamic_set = self.dynamic_set | (1 << a)
        else:
            if not self.has(a):
                copy_of_set = self.dynamic_set
                new_value = copy_of_set ^ (1 >> a)
                self.dynamic_set = new_value

    def remove(self, a):
        if a > self.size:
            raise IndexError("The value has been bigger than the list and it is not possible to "
                             "remove")
        else:
            if self.has(a):
                copy_of_set = self.dynamic_set
                new_value = copy_of_set ^ (1 << a)
                self.dynamic_set = new_value
                self.size = len(str(bin(self.dynamic_set))) - 2
            else:
                return False


if __name__ == '__main__':
    bit_vek = BitVektoren()
    bit_vek.insert(6)
    print(bin(bit_vek.dynamic_set))
    bit_vek.remove(6)
    print(bin(bit_vek.dynamic_set))
    print(bit_vek.has(6))
    print(bit_vek.size)


