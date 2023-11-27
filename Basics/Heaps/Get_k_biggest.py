

def get_values_bigger_x(x):

    visited = []
    queue = [1]
    while queue:
        curr_element = queue.pop(0)
        if curr_element <= len(H) - 1:
            if H[curr_element] >= x:
                visited.append(curr_element)
                queue.append(curr_element*2)
                queue.append(curr_element*2 + 1)

    print(visited)


if __name__ == '__main__':
    H = [0, 25, 13, 12, 3, 9, 7, 9, 2, 1, 5, 6]
    get_values_bigger_x(9)