"""Algorithm to find a two numbers in an array their addition is zero"""
import math
import random

# list with 100 random values
random_list = [random.randint(-29, 29) for i in range(30)]

def two_sum_slow(arr):
    """Brute force approach"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == 0 and i != j:
                return i, j
    return None

def two_sum_fast(arr):
    # sorting with merge sort for n log n runtime
    arr.sort()
    for i in range(len(arr)):
        start = 0
        end = len(arr)
        while start < end:
            mid = math.floor((start + end)/2)
            if arr[i] + arr[mid] == 0:
                return i, mid
            elif arr[i] + arr[mid] < 0:
                # search further on the right in the array
                start = mid + 1
            else:
                end = mid - 1
    return None


def three_sum_slow(arr):
    # i and j can be the same or i and m or j and m
    for i in range(len(arr)):
        for j in range(len(arr)):
            for m in range(len(arr)):
                if arr[i] + arr[j] + arr[m] == 0:
                    return i, j, m
    return None


def thrre_sum_faster(arr):
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(arr)):
            start = 0
            end = len(arr)
            while start < end:
                mid = math.floor((start + end) / 2)
                if arr[i] + arr[j] + arr[mid] == 0:
                    return i, j, mid
                elif arr[i] + arr[j] + arr[mid] < 0:
                    start = mid + 1
                else:
                    end = mid - 1

    return None


def three_sum_veryfast(arr):
    """Runtime goal of n^2"""
    arr.sort()
    for i in range(len(arr)):
        start = i
        end = len(arr) - 1
        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                return i, start, end
            elif arr[i] + arr[start] + arr[end] < 0:
                start += 1
            else:
                end -= 1
    return None


random_list = [-100, -99, -98, -97, -3, -3, 1, 1, 1, 1, 2, 3, 4, 5, 7]
res = three_sum_veryfast(random_list)
print(res)
print(random_list)
print(random_list[res[0]], random_list[res[1]], random_list[res[2]])
