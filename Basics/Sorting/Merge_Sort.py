"""Merge Sort Algorithm"""

import random


def merge_sort(arr):
    """Merge Sort Algorithm"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] == right[j]:
                print(left[i], right[j])
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    random_list = [random.randint(1, 29) for i in range(30)]
    print(random_list)
    print(merge_sort(random_list))
