class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = [1 for _ in range(len(s))]
        current_max = 0
        max_string = ""
        for index, letter in enumerate(s):
            if index > 0:
                if s[index] == s[index - res[index - 1] - 1] and index - res[index - 1] - 1 >= 0:
                    res[index] = res[index - 1] + 2
                elif s[index] == s[index - res[index]] and (res[index - 1] % 2 == 0 or
                                                            res[index - 1] == 1):
                    res[index] = res[index-1] + 1
                elif s[index] == s[index - res[index - 1]] and res[index - 1] % 2 == 1:
                    changed = True
                    for i in range(index - res[index - 1] + 1, index):
                        if not s[i] == s[index]:
                            res[index] = 1
                            changed = False
                            break
                    if changed:
                        res[index] = res[index - 1] + 1

            if res[index] > len(max_string):
                max_string = s[index - res[index] + 1:index + 1]
        return max_string


if __name__ == '__main__':
    c = Solution()
    print(c.longestPalindrome("cccccc"))
