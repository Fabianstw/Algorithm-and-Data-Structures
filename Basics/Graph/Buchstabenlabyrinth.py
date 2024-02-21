"""
Create an algorithm that finds the fastest way from the top left to the bottom right
You have to visit a then b
"""
import math


def fastest_way_brute_force(matrix, z=0, s=0, curr_letter="x"):
    if z == len(matrix) - 1 and s == len(matrix) - 1:
        return 1

    if curr_letter == "x":
        curr_letter = "b" if matrix[z][s] == "a" else "a"

    if z < 0 or z >= len(matrix) or s < 0 or s >= len(matrix):
        return math.inf

    if matrix[z][s] == curr_letter or matrix[z][s] == "y":
        return math.inf

    matrix[z][s] = "y"
    next_letter = "a" if curr_letter == "b" else "b"
    return 1 + min(
            fastest_way_brute_force(matrix, z + 1, s, next_letter),
            fastest_way_brute_force(matrix, z - 1, s, next_letter),
            fastest_way_brute_force(matrix, z, s + 1, next_letter),
            fastest_way_brute_force(matrix, z, s - 1, next_letter)
        )


def fastest_way(matrix):
    pass
# fast variant of the algorithm in BFS.py


if __name__ == '__main__':

    test_list = [["A", "A", "A", "B", "A"], ["B", "B", "B", "B", "B"], ["A", "A", "A", "A", "A"],
                 ["B", "B", "B", "B", "B"], ["A", "B", "A", "A", "A"]]

    # make the same list but with lower case letters
    test_list = [[x.lower() for x in y] for y in test_list]

    print(fastest_way_brute_force(test_list))
