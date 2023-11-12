""""""

from typing import List

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for i in range(2, numRows):
            new_list = [1]
            for j in range(i - 1):
                new_list.append(res[i-1][j] + res[i-1][j + 1])
            new_list.append(1)
            res.append(new_list)

        return res


    def generate_rek(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        last_list = self.generate_rek(numRows - 1)
        new_list = [1]
        for i in range(len(last_list[len(last_list) - 1]) - 1):
            new_list.append(last_list[len(last_list)-1][i] + last_list[len(last_list)-1][i+1])
        new_list.append(1)
        last_list.append(new_list)
        return last_list

if __name__ == '__main__':
    c = Solution()
    print(c.generate(5))
