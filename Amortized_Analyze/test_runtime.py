"""
Test the runtime for the amortized analysis
"""


def task1(n):
    summe = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0 and i != 1:
            summe += 2*i
        else:
            summe += 1

    return summe


def zweierpotenz(n):
    summe = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0 and i != 1:
            summe += i

    return summe


if __name__ == '__main__':
    print(zweierpotenz(1024))
