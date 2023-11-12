"""
Today: 12.11.2023
9. Palindrome Number
"""


class Solution:
    def isPalindrome2(self, x: int) -> bool:
        x = str(x)
        sx = len(x)
        for i in range(len(x) // 2):
            if x[i] != x[sx - 1 - i]:
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome(-121))

