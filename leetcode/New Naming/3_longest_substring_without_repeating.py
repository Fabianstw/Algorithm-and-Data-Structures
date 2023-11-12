class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_max = ""
        start, end = 0, 1
        while start < len(s) - 1:
            if len(s[start:end]) == len(set(s[start:end])):
                if len(s[start:end]) > len(current_max):
                    current_max = s[start:end]
                end += 1
                if end > len(s):
                    return len(current_max)
            else:
                start += 1
                if start >= end:
                    end = start + 1

        return len(current_max)


if __name__ == '__main__':
    c = Solution()
    print(c.lengthOfLongestSubstring("au"))
