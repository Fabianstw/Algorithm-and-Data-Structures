"""74 search a 2d matrix"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_start = 0
        row = 0
        while row_start < len(matrix):
            if matrix[row_start][0] <= target <= matrix[row_start][len(matrix[0])-1]:
                row = row_start
                break
            row_start += 1

        start, end = 0, len(matrix[0])
        while start < end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                if mid == start or mid == end:
                    start += 1
                else:
                    start = mid
            else:
                if mid == start or mid == end:
                    end -= 1
                else:
                    end = mid

        return False


if __name__ == '__main__':
    c = Solution()
    print(c.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23))