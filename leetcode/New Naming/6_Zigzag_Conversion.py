import math

"""
Most ugly possible solution
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        matrix = [["" for _ in range(math.ceil(len(s)/numRows) + (len(s)//numRows)*(numRows-1))] for _ in range(numRows)]

        counter = 0
        tmp_counter = numRows
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if counter >= len(s):
                    res = ""
                    for m in matrix:
                        res += "".join(m)
                    return res
                if tmp_counter == numRows or tmp_counter == 1:
                    matrix[j][i] = s[counter]
                else:
                    matrix[tmp_counter - 1][i] = s[counter]
                    counter += 1
                    break

                counter += 1

            tmp_counter -= 1
            if tmp_counter <= 1:
                tmp_counter = numRows

        res = ""
        for m in matrix:
            res += "".join(m)
        return res



if __name__ == '__main__':
    c = Solution()
    print(c.convert("A", 2))

