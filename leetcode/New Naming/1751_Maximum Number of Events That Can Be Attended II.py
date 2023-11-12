"""Leetcode"""
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # sort the events by start time
        events.sort(key=lambda x: x[2])
        events.reverse()
        if k == 1:
            return events[0][2]

        res_lst = [0 for _ in range(len(events))]

        for index, event in enumerate(events):
            current_times = [[event[0], event[1]]]
            value = event[2]
            counter = 1
            for next_index in range(index + 1, len(events)):
                # check if the next event has problems with current_times for alle the values in current_times
                for time in current_times:
                    attend_possible = True
                    if events[next_index][0] <= time[0] <= events[next_index][1] or events[next_index][0] <= time[1] <= \
                            events[next_index][1] or time[0] <= events[next_index][0] <= time[1] or time[0] <= \
                            events[next_index][1] <= time[1]:
                        attend_possible = False
                        break
                if attend_possible:
                    current_times.append([events[next_index][0], events[next_index][1]])
                    value += events[next_index][2]
                    counter += 1
                if counter == k:
                    break
            res_lst[index] = value
        print(res_lst)
        return max(res_lst)


if __name__ == '__main__':
    c = Solution()
    print(c.maxValue(
        [[44, 81, 11], [31, 41, 14], [85, 90, 5], [42, 78, 68], [46, 61, 11], [23, 92, 6], [64, 67, 70], [77, 92, 32],
         [5, 26, 87], [10, 44, 78], [18, 90, 40], [15, 65, 66], [1, 10, 29], [36, 80, 80], [3, 94, 5], [2, 62, 90],
         [19, 28, 47]], 16))
