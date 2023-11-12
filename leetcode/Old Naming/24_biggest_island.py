"""Find the biggest island in a matrix"""
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    visited = []
    max_points = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i - 1 >= 0 and j - 1 >= 0:
                    if grid[i - 1][j] != 0 and grid[i][j - 1] == 0:
                        grid[i][j] = grid[i - 1][j]
                    elif grid[i - 1][j] == 0 and grid[i][j - 1] != 0:
                        grid[i][j] = grid[i][j - 1]
                    elif grid[i - 1][j] != 0 and grid[i][j - 1] != 0:
                        if grid[i - 1][j] != grid[i][j - 1]:
                            print(i, j)
                            try:
                                visited.remove([grid[i][j - 1]])
                                visited.remove([grid[i - 1][j]])
                            except ValueError:
                                pass
                            visited.append([grid[i - 1][j], grid[i][j - 1]])
                            grid[i][j] = grid[i - 1][j]
                        else:
                            grid[i][j] = grid[i - 1][j]
                    else:
                        if len(visited) == 0:
                            grid[i][j] = 2
                            visited.append([2])
                            max_points.append(2)
                        else:
                            new_point = max(max_points) + 1
                            grid[i][j] = new_point
                            visited.append([new_point])
                            max_points.append(new_point)
                elif i == 0 and j != 0:
                    if grid[i][j - 1] != 0:
                        if grid[i][j - 1] > 1:
                            grid[i][j] = grid[i][j - 1]
                    else:
                        if len(visited) == 0:
                            grid[i][j] = 2
                            visited.append([2])
                            max_points.append(2)
                        else:
                            new_point = max(max_points) + 1
                            grid[i][j] = new_point
                            visited.append([new_point])
                            max_points.append(new_point)
                elif j == 0 and i != 0:
                    if grid[i - 1][j] != 0:
                        if grid[i - 1][j] > 1:
                            grid[i][j] = grid[i - 1][j]
                    else:
                        if len(visited) == 0:
                            grid[i][j] = 2
                            visited.append([2])
                            max_points.append(2)
                        else:
                            new_point = max(max_points) + 1
                            grid[i][j] = new_point
                            visited.append([new_point])
                            max_points.append(new_point)
                else:
                    if len(visited) == 0:
                        grid[i][j] = 2
                        visited.append([2])
                        max_points.append(2)
                    else:
                        new_point = max(max_points) + 1
                        grid[i][j] = new_point
                        visited.append([new_point])
                        max_points.append(new_point)

    print("")
    print(visited)
    for g in grid:
        print(g)

    gruppen = []
    for lst in visited:
        gefunden = False
        for gruppe in gruppen:
            if any(elem in gruppe for elem in lst):
                gruppe.extend(lst)
                gefunden = True
                break
        if not gefunden:
            gruppen.append(lst)

    gruppen_2 = []
    for lst in gruppen:
        gefunden = False
        for gruppe in gruppen_2:
            if any(elem in gruppe for elem in lst):
                gruppe.extend(lst)
                gefunden = True
                break
        if not gefunden:
            gruppen_2.append(lst)

    gruppen_3 = []
    for lst in gruppen_2:
        gefunden = False
        for gruppe in gruppen_3:
            if any(elem in gruppe for elem in lst):
                gruppe.extend(lst)
                gefunden = True
                break
        if not gefunden:
            gruppen_3.append(lst)

    gruppen_4 = []
    for lst in gruppen_3:
        gefunden = False
        for gruppe in gruppen_4:
            if any(elem in gruppe for elem in lst):
                gruppe.extend(lst)
                gefunden = True
                break
        if not gefunden:
            gruppen_4.append(lst)

    print(gruppen_4)

    max_res = 0
    for vis in gruppen_4:
        calc = 0
        vis_2 = list(set(vis))
        for v in vis_2:
            for g in grid:
                calc += g.count(v)
        if calc > max_res:
            max_res = calc

    return max_res


if __name__ == '__main__':
    matrix = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    matrix_2 = [[0, 1], [1, 1], [1, 1]]
    matrix_3 = [[0, 0, 1], [0, 1, 1], [1, 0, 0]]
    matrix_4 = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
    matrix_5 = [[1, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0, 1]]
    matrix_6 = [[0, 0, 0], [1, 0, 1]]
    matrix_7 = [[0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 1],
                [0, 1, 1, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [0, 1, 1, 0, 1, 0, 0, 0]]

    print(maxAreaOfIsland(grid=matrix_5))
