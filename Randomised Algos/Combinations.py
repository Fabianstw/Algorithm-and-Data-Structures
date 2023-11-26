from itertools import permutations

# Your array
my_array = [1, 2, 3, 4, 5, 6, 7]

# Get all permutations
all_permutations = permutations(my_array)

# Convert the permutations to a list (if needed)
all_permutations_list = list(all_permutations)

# Print the result
res = all_permutations_list

ans = []
for re in res:

    if re[2] == 3 or re[3] == 3 or re[4] == 3 or re[2] == 4 or re[3] == 4 or re[4] == 4 or re[2] == 5 or re[3] == 5 or re[4] == 5:
        ans.append(re)

def faku(n):
    if n == 0:
        return 1
    else:
        return n*faku(n-1)


def n_over_k(n, k):
    return faku(n)/(faku(k)*faku(n-k))


res = 0
for x in range(0, 8):
    for y in range(0, 8):
        for z in range(0, 8):
            if x+y+z == 7:
                res += (1/4)**x * (1/2)**y * (1/4)**z * ((faku(x)+faku(y)+faku(z))/faku(7))

res2 = 0
for x in range(0, 4):
    for y in range(1, 8):
        for z in range(0, 4):
            if x+y+z == 7:
                res2 += (1/4)**x * (1/2)**y * (1/4)**z * ((faku(x)+faku(y)+faku(z))/faku(7))

print(res)
print(res2)
print(res2/res)

