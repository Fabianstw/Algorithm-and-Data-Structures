"""Reverse the words in a string, but keep the string"""


def reverseWords(s: str) -> str:
    word_list = s.split()
    res = ""
    for word in word_list:
        res += word[-1:-len(word)-1:-1] + " "
    return res[:len(res)-1]


print(reverseWords("Let's take LeetCode contest"))