class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k > len(s):
            return len(s)
        elif k == 0:
            start, end = 0, 1
        else:
            start, end = 0, k
        current_max = 0
        map = {}
        for letter in s[start:end]:
            if letter in map:
                map[letter] += 1
            else:
                map.update({letter: 1})
        while start < len(s):
            end_inc = False
            for m in map:
                if (end - start) - map[m] <= k:
                    if end - start > current_max:
                        current_max = end - start
                    end += 1
                    end_inc = True
                    if end > len(s):
                        return current_max
                    if s[end-1] in map:
                        map[s[end-1]] += 1
                    else:
                        map.update({s[end-1]: 1})
                    break
            if end_inc is False:
                start += 1
                map[s[start-1]] -= 1

        return current_max


if __name__ == '__main__':
    c = Solution()
    # print(c.characterReplacement("ABBB", 2))
    print(c.characterReplacement("ABAA", 0))
