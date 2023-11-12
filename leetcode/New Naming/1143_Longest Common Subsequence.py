
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        calc_matrix = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        calc_matrix[i][j] = 1
                    else:
                        calc_matrix[i][j] = calc_matrix[i-1][j-1] + 1
                else:
                    if i == 0 and j == 0:
                        pass
                    elif i == 0:
                        calc_matrix[i][j] = calc_matrix[i][j - 1]
                    elif j == 0:
                        calc_matrix[i][j] = calc_matrix[i - 1][j]
                    else:
                        calc_matrix[i][j] = max(calc_matrix[i - 1][j - 1],
                                                calc_matrix[i - 1][j],
                                                calc_matrix[i][j - 1])
        print("   ", end="")
        for letter in text2:
            print(letter, end="  ")
        print()
        for i, m in enumerate(calc_matrix):
            print(text1[i], end=" ")
            print(m)
        return calc_matrix[len(calc_matrix) - 1][len(calc_matrix[0]) - 1]



if __name__ == '__main__':
    c = Solution()
    print(c.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr"))