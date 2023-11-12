"""Find the longest substring in string without repeating chars"""


def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    i = 0
    while i <= len(s):
        sub = set()
        for j in range(i, len(s)):
            if s[j] not in sub:
                sub.add(s[j])
            else:
                i = j - 1
                break

        if max_length < len(sub):
            max_length = len(sub)
        i += 1

    return max_length


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abbcd"))
