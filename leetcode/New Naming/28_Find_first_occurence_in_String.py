"""
Today: 13.11.2023
9. Find the first occurrence in a String
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle) + i] == needle:
                return i

        return -1


if __name__ == '__main__':
    c = Solution()
    print(c.strStr("sadbutsad", "but"))
