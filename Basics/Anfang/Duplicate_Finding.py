"""Algorithm to find one pair of duplicate elements in a list"""

import random
# liste mit 100 zufälligen werten
random_list = [random.randint(1, 29) for i in range(30)]
# liste mit 100 zufälligen werten
random_list_2 = [random.randint(1, 29) for i in range(30)]


def o_nxn(arr):
    """Laufzeit von O(n^2)"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                return i, j


if __name__ == '__main__':
    print(random_list)
    print(o_nxn(random_list))
    print(random_list_2)
