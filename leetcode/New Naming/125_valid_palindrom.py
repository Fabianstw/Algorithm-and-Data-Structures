"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalpha() and not s[i].isnumeric():
                i += 1
            elif not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1
        return True


if __name__ == '__main__':
    c = Solution()
    print(c.isPalindrome("A0"))
