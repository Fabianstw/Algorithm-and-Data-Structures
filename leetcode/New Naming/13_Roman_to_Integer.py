"""
Today: 12.11.2023
13. Roman to Integer
"""


class Solution:
    def romanToInt2(self, s: str) -> int:
        res, i = 0, 0
        while i < len(s):
            if s[i] == "M":
                res += 1000
            elif s[i] == "D":
                res += 500
            elif s[i] == "C":
                if i != len(s) - 1:
                    if s[i+1] == "M":
                        res += 900
                        i += 1
                    elif s[i+1] == "D":
                        res += 400
                        i += 1
                    else:
                        res += 100
                else:
                    res += 100
            elif s[i] == "L":
                res += 50
            elif s[i] == "X":
                if i != len(s) - 1:
                    if s[i + 1] == "C":
                        res += 90
                        i += 1
                    elif s[i + 1] == "L":
                        res += 40
                        i += 1
                    else:
                        res += 10
                else:
                    res += 10
            elif s[i] == "V":
                res += 5
            else:
                if i != len(s) - 1:
                    if s[i+1] == "X":
                        res += 9
                        i += 1
                    elif s[i+1] == "V":
                        res += 4
                        i += 1
                    else:
                        res += 1
                else:
                    res += 1
            i += 1

        return res

    def romanToInt(self, s: str) -> int:

        m = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        res = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]
        return res


if __name__ == '__main__':
    c = Solution()
    print(c.romanToInt("MCMXCIV"))

