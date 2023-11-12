"""

"""
import math

first_line = input().split()
friends = int(first_line[0])
pubs = int(first_line[1])

pubs_list = []
# 0 = h 1 = m
for i in range(pubs):
    x, y = input().split()
    pubs_list.append([int(x), int(y)])

h_list = pubs_list[:]
h_list.sort(key=lambda x: x[0], reverse=True)
m_list = pubs_list[:]
m_list.sort(key=lambda x: x[1], reverse=True)

h_left, m_left = friends, friends
changes = -1

while True:
    changes += 1
    if h_left > 0:
        ml_found = False
        for i in range(len(m_list)):
            if m_list[i][1] >= h_left:
                m_left -= m_list[i][1]
                ml_found = True
                m_list.pop(i)
                break
        if not ml_found:
            for i in range(len(h_list)):
                if h_list[i][0] >= h_left:
                    h_left -= h_list[i][0]
                    h_list.pop(i)
                    break
    elif m_left > 0:
        m_left -= m_list[0][1]
        m_list.pop(0)
    else:
        break

print(changes)

