""""""

from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s2) + len(s1) != len(s3):
            return False
        if s3 == "":
            return True

        dp = {}

        def helper(index_1, index_2, index_3):
            if (index_1, index_2, index_3) in dp:
                return dp[(index_1, index_2, index_3)]
            if index_3 == len(s3) - 1:
                return True
            if index_1 >= len(s1):
                if s2[index_2] == s3[index_3]:
                    dp.update({(index_1, index_2, index_3):
                                    helper(index_1, index_2 + 1, index_3 + 1)})
                    return dp[(index_1, index_2, index_3)]
                return False
            if index_2 >= len(s2):
                if s1[index_1] == s3[index_3]:
                    dp.update({(index_1, index_2, index_3):
                                   helper(index_1 + 1, index_2, index_3 + 1)})
                    return dp[(index_1, index_2, index_3)]
                return False

            if s1[index_1] == s3[index_3] and s2[index_2] == s3[index_3]:
                dp.update({(index_1, index_2, index_3): helper(index_1 + 1, index_2, index_3 + 1)
                                                        or helper(index_1, index_2 + 1, index_3 + 1)})
                return dp[(index_1, index_2, index_3)]
            if s1[index_1] == s3[index_3]:
                dp.update({(index_1, index_2, index_3):
                               helper(index_1 + 1, index_2, index_3 + 1)})
                return dp[(index_1, index_2, index_3)]
            if s2[index_2] == s3[index_3]:
                dp.update({(index_1, index_2, index_3):
                               helper(index_1, index_2 + 1, index_3 + 1)})
                return dp[(index_1, index_2, index_3)]
            return False

        return helper(0, 0, 0)


if __name__ == '__main__':
    c = Solution()
    print(c.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
