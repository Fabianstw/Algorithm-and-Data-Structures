class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # remove all # in s and the letter before it
        s = list(s)
        t = list(t)
        i, j = 0, 0
        while True:
            if 0 <= i < len(s):
                if s[i] == '#':
                    s.pop(i)
                    if i > 0:
                        s.pop(i-1)
                    i -= 1
                    if i < 0:
                        i = 0
                else:
                    i += 1
            if 0 <= j < len(t):
                if t[j] == '#':
                    t.pop(j)
                    if j > 0:
                        t.pop(j-1)
                    j -= 1
                    if j < 0:
                        j = 0
                else:
                    j += 1

            if i >= len(s) and j >= len(t):
                break

        if s == t:
            return True
        return False


if __name__ == '__main__':
    c = Solution()
    print(c.backspaceCompare("a##c", "a#c#"))
