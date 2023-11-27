"""Algo Summen Datenstruktur"""


from typing import List


class slow_datastructur:

    def __init__(self, field):
        self.field = field
        self.lower_field = [0 for _ in range(len(self.field))]
        self.__prepare_sum()

    def __prepare_sum(self):
        tmp_l, tmp_r = 0, 0
        for i in range(len(self.field)):
            tmp_l += self.field[i]
            tmp_r += self.field[len(self.field) - 1 - i]
            self.lower_field[i] = tmp_l

        print(self.lower_field)

    def re_sum(self, i, j):
        if i > 0:
            return self.lower_field[j] - self.lower_field[i-1]
        else:
            return self.lower_field[j]

    def change(self, i, x):
        self.field[i] = x
        self.__prepare_sum()


if __name__ == '__main__':
    d = slow_datastructur([1,2,3,4])
    print(d.re_sum(1, 3))

