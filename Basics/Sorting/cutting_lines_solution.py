"""Merge Sort to specific target"""


def merge_to_target(lst, target_lst):
    """
    Merge Sort lst to look the same as target_lst
    :param lst:
    :param target_lst:
    :return:
    """
    if len(lst) <= 1:
        return lst, 0

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted, inversions_left = merge_to_target(left, target_lst)
    right_sorted, inversions_right = merge_to_target(right, target_lst)
    inversions = inversions_right + inversions_left
    result = []
    i, j = 0, 0
    while i < len(left_sorted) and j < len(right_sorted):
        if target_lst[left_sorted[i]] <= target_lst[right_sorted[j]]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1
            inversions += (len(left_sorted) - i)
    result += left_sorted[i:]
    result += right_sorted[j:]
    return result, inversions


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

target_list = dict()
for q in q_new:
    target_list[q] = q_new.index(q)

sorted_1, count = merge_to_target(p_new, target_list)
print(sorted_1, count)
