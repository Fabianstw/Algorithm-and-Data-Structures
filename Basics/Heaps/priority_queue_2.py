"""Priority Queue using a heap and a list"""
import math


class priority_queue:

    def __init__(self):
        self.heap = [None]
        self.size = 0

    def max(self):
        return self.heap[1]

    def remove_largestm(self, m):

        tmp = []

        while True:

            if self.max() < m:
                print(tmp)
                for i in range(len(tmp) - 1):
                    self.insert(tmp[i])
                return
            else:
                tmp.append(self.extract_max())

    def extract_max(self):
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.bubble_down(1)
        return max

    def bubble_down(self, i):
        while i * 2 <= self.size:
            child = self.max_child(i)
            if self.heap[i] < self.heap[child]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child

    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def bubble_up(self, i):
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.bubble_up(self.size)

    def increase_key(self, i, key):
        if key < self.heap[i]:
            raise ValueError("New key is smaller than current key")
        self.heap[i] = key
        self.bubble_up(i)

    def decrease_key(self, i, key):
        if key > self.heap[i]:
            raise ValueError("New key is bigger than current key")
        self.heap[i] = key
        self.bubble_down(i)

    def delete(self, x):
        self.heap[x] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.bubble_down(x)

    def fusion(self, x, y):
        x_value, y_value = self.heap[x], self.heap[y]
        self.delete(y)
        self.heap[x] = x_value + y_value
        self.bubble_down(x)

    def print(self):
        print("This is the priority queue: ")
        for i in range(1, self.size + 1):
            print(self.heap[i], end=" ")
            # when i is 2^k - 1, print a new line
            if i == 2 ** int(math.log(i, 2) + 1) - 1:
                print()
        print("\nThis was the priority queue")


if __name__ == '__main__':
    # with 10 elements between 1 and 100
    c = priority_queue()
    c.insert(1)
    c.insert(2)
    c.insert(25)
    c.insert(4)
    c.insert(10)
    c.insert(5)
    c.insert(33)
    c.insert(7)
    c.insert(18)
    c.insert(100)
    c.print()
    print(c.max())
    print(c.extract_max())
    c.increase_key(5, 1000)
    c.insert(2000)
    c.print()
    c.delete(2)
    c.print()
    c.fusion(2, 7)
    print()
    c.print()
    c.remove_largestm(23)
    c.print()
