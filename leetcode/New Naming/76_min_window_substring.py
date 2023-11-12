class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = dict()
        for letter in range(len(t)):
            if s[letter] in map:
                map[s[letter]] += 1
            else:
                map.update({s[letter]: 1})

        start, end = 0, len(t)
        while True:
            pass


# code on leetcode



if __name__ == '__main__':
    c = Solution()
    print(c.minWindow(s="cabwefgewcwaefgcf", t="cae"))
