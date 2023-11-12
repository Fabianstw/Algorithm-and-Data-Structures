import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap_list = []
        heapq.heapify(heap_list)

        result = []
        used = set()

        heapq.heappush(heap_list, 1)
        while len(result) < n:
            value = heapq.heappop(heap_list)
            result.append(value)
            used.add(value)
            if value * 2 not in used:
                heapq.heappush(heap_list, value * 2)
                used.add(value * 2)
            if value * 3 not in used:
                heapq.heappush(heap_list, value * 3)
                used.add(value * 3)
            if value * 5 not in used:
                heapq.heappush(heap_list, value * 5)
                used.add(value * 5)

        return int(result[n-1])


class Heap_Number:

    def __init__(self):
        self.heap = [-float('inf')]

    def add_number(self, num):
        self.heap.append(num)
        self.bubble_up(len(self.heap) - 1)

    def get_min(self):
        if len(self.heap) > 1:
            value = self.heap[1]
            self.heap[1] = self.heap[len(self.heap) - 1]
            self.heap.pop()
            self.bubble_down(1)
            return value

    def bubble_up(self, index):
        if self.heap[index] < self.heap[index // 2]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            self.bubble_up(index // 2)

    def bubble_down(self, index):
        # bubble down heap
        if index * 2 < len(self.heap):
            if index * 2 + 1 < len(self.heap):
                if self.heap[index * 2] < self.heap[index * 2 + 1]:
                    if self.heap[index] > self.heap[index * 2]:
                        self.heap[index], self.heap[index * 2] = self.heap[index * 2], self.heap[index]
                        self.bubble_down(index * 2)
                else:
                    if self.heap[index] > self.heap[index * 2 + 1]:
                        self.heap[index], self.heap[index * 2 + 1] = self.heap[index * 2 + 1], self.heap[index]
                        self.bubble_down(index * 2 + 1)
            else:
                if self.heap[index] > self.heap[index * 2]:
                    self.heap[index], self.heap[index * 2] = self.heap[index * 2], self.heap[index]
                    self.bubble_down(index * 2)

if __name__ == '__main__':
    c = Solution()
    print(c.nthUglyNumber(210))
