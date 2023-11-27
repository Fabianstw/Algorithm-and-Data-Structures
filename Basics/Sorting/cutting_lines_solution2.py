



p_out = [4, 7, 3, 5, 1, 2, 6, 8]
q_out = [7, 3, 2, 5, 4, 1, 6, 8]

p_new = [0 for _ in range(len(p_out))]
for k in range(len(p_out)):
    p_new[p_out[k]-1] = k + 1

print(p_new)

q_new = [0 for _ in range(len(q_out))]
for k in range(len(q_out)):
    q_new[q_out[k]-1] = k + 1

print(q_new)