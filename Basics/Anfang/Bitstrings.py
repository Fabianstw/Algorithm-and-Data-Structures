"""Algo Blatt 3 Aufgabe Fehlende Bitstring"""
import random


def create_bitstrings(l, k):
    """
    Create list with 2^l diffrent values only 0,1 containing as String iterativ
    :param l:
    :param k:
    :return:
    """
    creation_bit_lst = []
    for i in range((2 ** l)):
        creation_bit_lst.append(bin(i)[2:].zfill(l))
    random.shuffle(creation_bit_lst)
    for _ in range(k):
        creation_bit_lst.pop()
    return creation_bit_lst


def fetch_bit(arr, i, j):
    """
    :param arr:
    :param i:
    :param j:
    :return: j Bit of A[i]
    """
    return arr[i][j]


def find_missing_bit(arr, l, k):
    """
    Finds the missing bit of the arr
    Has only runtime of O(n) because l is a constant and it is not important in the O Notation
    n will alway be much bigger, especially when k is only 1
    :param arr:
    :return:
    """
    calc = 0
    for i in range(len(arr)):
        calc_1 = []
        for j in range(l):
            calc_1.append(fetch_bit(arr, i, j))
        calc_2 = "".join(calc_1)
        calc += int(calc_2, 2)

    pow_base = sum([x for x in range((2 ** l))])
    result = str(bin(pow_base - calc))[2:]
    return result


l = 3
k = 1
bit_list = create_bitstrings(l, k)
print(bit_list)
print(len(bit_list))

print(fetch_bit(bit_list, 1, 0))

miss_bit = find_missing_bit(bit_list, l, k)
print(miss_bit)
