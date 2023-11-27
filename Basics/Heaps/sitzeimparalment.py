"""Sitze im Parlament Aufgabe Algo"""


import heapq


class Prio_queue:

    def __init__(self):
        self.heap = [(-9999, -9999)]
        self.size = 0

    def insert(self, key, value):
        self.heap.append((key, value))
        self.size += 1
        self.bubble_up(self.size)

    def increase_key(self, i, key):
        if key < self.heap[i][0]:
            raise ValueError("New key is smaller than current key")
        self.heap[i] = (key, self.heap[i][1])
        self.bubble_up(i)

    def get_max(self):
        return self.heap[1]

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
            if self.heap[i][0] < self.heap[child][0]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child

    def bubble_up(self, i):
        while i // 2 > 0:
            if self.heap[i][0] > self.heap[i // 2][0]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i * 2][0] > self.heap[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def print_heap(self):
        print(self.heap)


def calc_places(data):
    parties, sits = int(data[0].split(" ")[0]), int(data[0].split(" ")[1])
    p_queue = Prio_queue()
    for i in range(1, len(data)):
        p_queue.insert(int(data[i]), i)
    result_list = [0 for _ in range(parties + 1)]
    for i in range(sits):
        q, i = p_queue.extract_max() # log n
        result_list[i] += 1
        p_queue.insert(q * result_list[i] / (result_list[i] + 1), i)
    return result_list[1:]


def calculate_seating_arrangement(data):
    parties, sits = map(int, data[0].split(" "))
    p_queue = []
    heapq.heapify(p_queue)
    for i in range(1, len(data)):
        heapq.heappush(p_queue, (-int(data[i]), i))
    result_list = [0] * (parties + 1)
    for i in range(sits):
        q, j = heapq.heappop(p_queue)
        q = -q
        result_list[j] += 1
        heapq.heappush(p_queue, (-q * result_list[j] / (result_list[j] + 1), j))
    return result_list[1:]


def read_files():
    res = []
    # file_path = "/Users/fabian/Desktop/Python/Semester 2/Algo 1/seatallocation-tests-v2/v2-014-19.in"
    file_path = "/Users/fabian/Desktop/Python/Semester 2/Algo 1/seatallocation-tests-v2/v2-015-secret.in"
    file = open(file_path, "r")
    for i, line in enumerate(file):
        res.append(line.rstrip())
    return res

def save_line_for_line(res):
    with open('output.txt', 'w') as file:
        for line in res:
            file.write(str(line) + '\n')


if __name__ == '__main__':
    file1 = read_files()
    print("TEST")
    res = calculate_seating_arrangement(file1)
    print(res)
    save_line_for_line(res)

    # sha1sum for the secret part is
    # d55a0825e177f629b275028c098e9d0309718656
