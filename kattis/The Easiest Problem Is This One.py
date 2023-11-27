"""alshkbd."""


inputs = []
while True:
    x = int(input())
    if x != 0:
        inputs.append(x)
    else:
        break


def sum_of_digits(num):
    res = 0
    num_str = str(num)
    for l in num_str:
        res += int(l)

    return res


for i in inputs:
    k = 11
    while sum_of_digits(i) != sum_of_digits(i*k):
        k += 1

    print(k)


