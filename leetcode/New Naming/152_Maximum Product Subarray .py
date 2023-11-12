""""""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        splitted = []
        values = []
        last_index = -1
        for index in range(len(nums)):
            if nums[index] == 0:
                new_list = nums[last_index + 1:index]
                if len(new_list) > 0:
                    splitted.append(new_list)
                else:
                    values.append(0)
                last_index = index

        if not last_index == len(nums) - 1:
            splitted.append(nums[last_index + 1:])
        else:
            values.append(0)

        print(splitted)
        if len(splitted) > 1:
            values.append(0)

        for split in splitted:
            count_n = 0
            if len(split) == 1:
                values.append(split[0])
                continue
            for s in split:
                if s < 0:
                    count_n += 1
            if count_n % 2 == 0:
                res = 1
                for sp in split:
                    res *= sp
                values.append(res)
            else:
                res_1, res_2, counter_1, counter_2 = 1, 1, 0, 0
                for spi in split:
                    if counter_2 >= 1:
                        res_2 *= spi
                    if spi < 0:
                        counter_1 += 1
                        counter_2 += 1
                    if counter_1 < count_n:
                        res_1 *= spi

                values.append(max(res_1, res_2))

        return max(values)

if __name__ == '__main__':
    c = Solution()
    print(c.maxProduct([3,-1,4]))
