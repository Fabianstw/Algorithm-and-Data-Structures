"""aöosdlj"""

num_spies = int(input())

spy_attr = [[] for _ in range(num_spies)]

for spy in range(num_spies):
    ava_attributes = int(input())
    for attr in range(ava_attributes):
        curr_attr = input()
        spy_attr[spy].append(curr_attr)


for current_spy in spy_attr:
    badges = dict()
    for curr_attr in current_spy:
        if curr_attr.split(" ")[1] in badges:
            badges[curr_attr.split(" ")[1]] += 1
        else:
            badges.update({curr_attr.split(" ")[1]: 1})

    result = 1
    for current_in_badges in badges:
        result *= (badges[current_in_badges] + 1)

    print(result - 1)

