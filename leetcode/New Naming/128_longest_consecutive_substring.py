

def longestConsecutive(nums):
    all_nums = set(nums)
    max_len = 0

    for num in nums:
        if num + 1 in all_nums:
            curr_len = 1
            curr_num = num
            while curr_num + 1 in all_nums:
                curr_len += 1
                curr_num += 1
            if max_len < curr_len:
                max_len = curr_len

    return max_len


if __name__ == '__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))