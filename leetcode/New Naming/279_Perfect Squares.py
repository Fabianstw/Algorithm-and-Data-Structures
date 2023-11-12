import math


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [0]
        visited = dict()
        counter = 0
        while queue:
            curr_queue = queue
            queue = []
            counter += 1
            for node in curr_queue:
                if node not in visited:
                    visited.update({node: counter})
                    if node == n:
                        return visited[node] - 1
                    for new_number in range(1, math.ceil(math.sqrt(n)) + 1):
                        num = node + new_number**2
                        if num == n:
                            return counter
                        if num not in visited:
                            queue.append(num)


if __name__ == '__main__':
    c = Solution()
    print(c.numSquares(12))