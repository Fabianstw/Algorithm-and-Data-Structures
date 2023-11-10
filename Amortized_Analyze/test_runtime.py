"""
Test the runtime for the amortized analysis
"""
import math


def task1(n):
    summe = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0 and i != 1:
            summe += 2*i
        else:
            summe += 1
            pass

    return summe


def zweierpotenz(n):
    summe = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0 and i != 1:
            summe += i

    return summe

def n_summation(n):
    summe = 0
    while n > 1:
        summe += n
        n //= 2

    return summe

def summation_logn(n):
    summe = 0
    i = 0
    while i <= math.log(n, 2):
        summe += 2**i
        i += 1
    return summe


if __name__ == '__main__':
    print(summation_logn(33554432)/33554432)

