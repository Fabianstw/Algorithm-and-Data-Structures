"""Check if valid soduko"""
import math
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    boxes = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(len(board)):
        double_row = set()
        double_col = set()
        for j in range(len(board)):
            if board[i][j] in double_row or board[j][i] in double_col or \
                    board[i][j] in boxes[math.floor(i/3)][math.floor(j/3)]:
                return False
            else:
                if board[i][j] != ".":
                    double_row.add(board[i][j])
                    boxes[math.floor(i / 3)][math.floor(j / 3)].add(board[i][j])
                if board[j][i] != ".":
                    double_col.add(board[j][i])

    return True


if __name__ == '__main__':
    print(isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                         [".", "4", ".", "3", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                         [".", ".", "2", ".", "7", ".", ".", ".", "."],
                         [".", "1", "5", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", "2", ".", ".", "."],
                         [".", "2", ".", "9", ".", ".", ".", ".", "."],
                         [".", ".", "4", ".", ".", ".", ".", ".", "."]]))

    print(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
