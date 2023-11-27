"""Register List"""
import math


class Register_low:

    def __init__(self):
        self.heap = [(None, None)]
        self.size = 1

    def move_up(self, i):
        if i == 1:
            return
        if self.heap[i][0] < self.heap[i//2][0]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            self.move_up(i//2)

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        left = self.heap[i * 2]
        right = self.heap[i * 2 + 1]
        if left[0] < right[0]:
            return i * 2
        else:
            return i * 2 + 1

    def move_down(self, i):
        if i >= self.size // 2:
            return
        if self.heap[self.min_child(i)][0] < self.heap[i][0]:
            min_child = self.min_child(i)
            self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
            self.move_down(min_child)

    def insert(self, snr, income):
        self.heap.append((income, snr))
        if len(self.heap) > 2:
            self.move_up(self.size)
        self.size += 1

    def deportlowestincome(self):
        if self.size == 0:
            return
        else:
            self.heap[1] = self.heap[self.size - 1]
            self.size -= 1
            self.heap.pop()
            self.move_down(1)


    def print(self):
        print("This is the priority queue: ")
        for i in range(1, self.size):
            print(self.heap[i], end=" ")
            # when i is 2^k - 1, print a new line
            if i == 2 ** int(math.log(i, 2) + 1) - 1:
                print()
        print("\nThis was the priority queue")



if __name__ == '__main__':
    register = Register_low()
    register.insert(1, 1)
    register.insert(2, 2)
    register.insert(3, 3)
    register.insert(4, 0)

    register.print()

    register.deportlowestincome()

    register.print()
