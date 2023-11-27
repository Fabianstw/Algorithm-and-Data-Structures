"""Maxmilae Teilfelder in einem Feld finden"""
import math
import random


def maximale_teilfelder_ntimesn(lst):
    max_sum = -99999999 # did not work with math.nan so did not want to try out much more
    max_ind = (0, 0)
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            curr_sum = sum(lst[i:j+1])
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_ind = (i, j)

    return max_sum, max_ind

def maximale_teilfelder_nlogn(lst):
    if len(lst) == 1:
        return lst[0]

    mid = len(lst) // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]
    left_max = maximale_teilfelder_nlogn(left_lst)
    right_max = maximale_teilfelder_nlogn(right_lst)

    cross_sum = 0
    cross_sum_left = -99999
    for i in range(mid - 1, -1, -1):
        cross_sum += lst[i]
        cross_sum_left = max(cross_sum, cross_sum_left)

    cross_sum = 0
    cross_sum_right = -99999
    for i in range(mid, len(lst)):
        cross_sum += lst[i]
        cross_sum_right = max(cross_sum, cross_sum_right)

    cross_left_right = cross_sum_right + cross_sum_left
    return max(cross_left_right, right_max, left_max)


# List with 100 random numbers between -100 and 100
random_list = [random.randint(-10, 10) for _ in range(20)]
random_list_2 = [random.randint(-10, -1) for _ in range(20)]

a, b = maximale_teilfelder_ntimesn(random_list)
c = maximale_teilfelder_nlogn(random_list)
print(random_list)
print(a)
print(b)
print(c)
