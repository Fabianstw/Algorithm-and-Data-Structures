"""Algorithm to find number of cutting lines"""
import copy
import math


def slow_algo(p, q):
    res = 0
    for i in range(len(p)):
        for j in range(len(p)):
            if p[j] > p[i] and q[j] < q[i]:
                res += 1
    return res


def fast_algo(p, q):
    res = 0
    for i in range(len(p)):
        pass


def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = int(len(arr)/2)
        a = arr[:mid]
        b = arr[mid:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions


if __name__ == '__main__':
    p_out = [4, 7, 3, 5, 1, 2, 6]
    q_out = [7, 3, 2, 5, 4, 1, 6]
