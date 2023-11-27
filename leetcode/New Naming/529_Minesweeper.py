"""
Leetcode 529. Minesweeper
"""
from typing import List


class Solution:
    dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        current_field = board[click[0]][click[1]]
        if current_field.isnumeric():
            return board
        if current_field == "M":
            board[click[0]][click[1]] = "X"
            return board
        if current_field == "E":
            queue = [(click[0], click[1])]
            visited = set()
            while queue:
                curr = queue.pop()
                count_mines = self.countmines(board, (curr[0], curr[1]))
                if count_mines > 0:
                    board[curr[0]][curr[1]] = str(count_mines)
                else:
                    board[curr[0]][curr[1]] = "B"
                    for neigh in self.dirs:
                        if len(board) > curr[0] + neigh[0] >= 0 and len(board[0]) > curr[1] + neigh[1] >= 0:
                            if board[curr[0] + neigh[0]][curr[1] + neigh[1]] == "E":
                                tmp = curr[0] + neigh[0], curr[1] + neigh[1]
                                if tmp not in visited:
                                    visited.add(tmp)
                                    queue.append(tmp)

        return board

    def countmines(self, board, click):
        count_mines = 0
        pos_1, pos_2 = click[0], click[1]
        for neigh in self.dirs:
            if len(board) > pos_1 + neigh[0] >= 0 and len(board[0]) > pos_2 + neigh[1] >= 0:
                if board[pos_1 + neigh[0]][pos_2 + neigh[1]] == "M":
                    count_mines += 1
        return count_mines


if __name__ == '__main__':
    c = Solution()
    print(c.updateBoard(
        [["E", "E", "E", "E", "E"],
         ["E", "E", "M", "E", "E"],
         ["E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E"]],
        [3, 0]))
