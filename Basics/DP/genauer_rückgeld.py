"""Genauer Rückgeld Aufgabe Algo"""
import math

options = [1, 4, 7, 13, 28, 52, 91, 365]


def greedy_variante(money, rounds):
    if money == 0:
        return rounds
    change = 0
    for i, option in enumerate(options):
        if option > money:
            change = options[i-1]
            break

    return greedy_variante(money-change, rounds+1)


def rek_variante(money, rounds):
    """Extreme shitty runtime, could not be worse"""
    if money < 0:
        return math.inf
    if money == 0:
        return rounds

    res = [rek_variante(money - option, rounds+1) for option in options]
    return min(res)


def iter_variante(n):
    res = [0]
    for i in range(1, n+1):
        res.append(10000)
        for option in options:
            if i - option == 0:
                res[i] = 1
                break
            if i - option > 0:
                if res[i] > 1 + res[i - option]:
                    res[i] = res[i - option] + 1
    return res


if __name__ == '__main__':
    print(greedy_variante(32, 0))
    # print(rek_variante(32, 0))
    print(iter_variante(32))
