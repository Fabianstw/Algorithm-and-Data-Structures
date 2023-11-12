"""Find the element which is floor n/2 times in the array"""
import math
from typing import List


def majorityElement(nums: List[int]) -> int:
    done = set()
    res_lst_1 = []
    res_lst_2 = []
    for num in nums:
        if num not in done:
            res = nums.count(num)
            res_lst_1.append(res)
            res_lst_2.append(num)
        done.add(num)

    return res_lst_2[res_lst_1.index(max(res_lst_1))]


if __name__ == '__main__':
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


