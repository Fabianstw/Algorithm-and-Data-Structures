"""Algo Abgabe Union Find Move"""

from typing import List


class Node:

    def __init__(self, value):
        self.value = value
        self.head = None
        self.next = None
        self.prev = None


class Union:

    def __init__(self, length):
        self.virt_heads = []
        self.mass = []
        self.tails = []
        for x in range(length):
            self.virt_heads.append(Node(x))
            self.mass.append(Node(x))
            self.mass[x].head = self.virt_heads[x]
            self.mass[x].prev = self.virt_heads[x]
            self.virt_heads[x].next = self.mass[x]
            self.tails.append(x)

    def query(self, s, t):

        if self.mass[s].head.value == self.mass[t].head.value:
            return 1
        return 0

    def union(self, s, t):
        if self.query(s, t) == 0:
            tail = self.tails[self.mass[s].head.value]
            self.tails[self.mass[s].head.value] = self.tails[t]
            self.mass[tail].next = self.mass[t]
            self.mass[t].prev = self.mass[tail]

            # head of t is now mass[s]
            self.mass[t].head = self.virt_heads[self.mass[s].head.value]
            # and this for alle the elements .next of t
            curr = self.mass[t]
            while curr.next is not None:
                curr.head = self.virt_heads[self.mass[s].head.value]
                curr = curr.next

    def move(self, s, t):
        if self.query(s, t) == 0:
            # move the head of s to the head of t
            self.mass[s].head = self.virt_heads[self.mass[t].head.value]

            curr = self.mass[s]
            if curr.next is not None and curr.prev is not None:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            elif curr.next is None and curr.prev is not None:
                curr.prev.next = None
                self.tails[self.mass[s].head.value] = curr.prev.value
            elif curr.next is not None and curr.prev is None:
                curr.next.prev = None
                self.virt_heads[self.mass[s].head.value].next = curr.next

            self.mass[self.tails[self.mass[s].head.value]].next = self.mass[s]
            self.tails[self.mass[s].head.value] = self.mass[s].value

    def print(self):
        # print each value of the list and the complete linked list
        for x in range(len(self.mass)):
            # print with --> between the values
            curr = self.mass[x]
            while curr is not None:
                print(curr.value, end="-->")
                curr = curr.next
            print("None")


def read_files():
    res = []
    file_path = "/Semester 2/Algo 1/UnionFind/unionfindmove-tests/030-largeblocks-move-lg.in"
    # file_path = "/Users/fabian/Desktop/Python/Semester 2/Algo 1/unionfindmove-tests/032-huge.in"
    print(file_path)
    file = open(file_path, "r")
    for i, line in enumerate(file):
        res.append(line.rstrip())
    return res


def save_line_for_line(res):
    with open('/Semester 2/Algo 1/output.txt', 'w') as file:
        for line in res:
            file.write(str(line) + '\n')


if __name__ == '__main__':
    file1 = read_files()
    union = Union(int(file1[0].split(" ")[0]))
    res = []
    for i in range(1, len(file1)):
        line = file1[i].split(" ")
        first, second, third = int(line[0]), int(line[1]), int(line[2])
        if first == 0:
            # print(union.query(second, third))
            res.append(union.query(second, third))
        elif first == 1:
            union.union(second, third)
        else:
            union.move(second, third)

    save_line_for_line(res)
