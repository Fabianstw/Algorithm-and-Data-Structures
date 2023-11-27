""" File to test insertion sort algorithm """
import random


def insertion_sort_small_to_big(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    return arr


def insertion_sort_big_to_small(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    return arr


random_list = [1, 5, 3, 2, 4, 6, 7, 8, 9, 10]

print(insertion_sort_small_to_big(random_list))

# random list with 100 values
random_list_2 = [random.randint(1, 100) for i in range(100)]
print(insertion_sort_big_to_small(random_list_2))
