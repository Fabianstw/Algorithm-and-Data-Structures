"""Product of Array Except Self"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:

    pre_fix = [1]
    length = len(nums) - 1
    post_fix = [0 for _ in range(length + 1)]
    for i in range(len(nums)):
        pre_fix.append(pre_fix[len(pre_fix) - 1]*nums[i])
        if i != 0:
            post_fix[length - i] = post_fix[length - i + 1]*nums[length - i]
        else:
            post_fix[length - i] = nums[length - i]
    pre_fix = pre_fix[1:]
    res = []
    for j in range(length + 1):
        if j == 0:
            res.append(post_fix[1])
        elif j == length:
            res.append(pre_fix[j - 1])
        else:
            res.append(pre_fix[j - 1]*post_fix[j + 1])

    return res


if __name__ == '__main__':
    productExceptSelf([1,2,0,4])