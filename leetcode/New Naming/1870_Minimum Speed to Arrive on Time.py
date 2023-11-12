from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        start, end = 1, max(dist) * 100

        while start < end:
            mid = (start + end) // 2
            if self.check_arrive_time(dist, mid) <= hour:
                end = mid
            else:
                start = mid + 1

        return start if self.check_arrive_time(dist, start) <= hour else -1

    def check_arrive_time(self, dist, speed):
        time = 0
        for d in dist[:-1]:
            time += d // speed
            if d % speed != 0:
                time += 1
        time += dist[-1] / speed
        return time


if __name__ == '__main__':
    c = Solution()
    print(c.minSpeedOnTime([1,1,100000], 2.01))