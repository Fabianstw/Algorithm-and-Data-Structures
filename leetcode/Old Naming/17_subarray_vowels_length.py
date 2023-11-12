"""Count the number of vowel lettes in a substring with the length k"""


def maxVowels(s: str, k: int) -> int:
    res = 0

    if len(s) == 0:
        return 0

    for i in range(len(s) - k + 1):
        calc = s[i:i + k].count("a") + s[i:i + k].count("e") + s[i:i + k].count("i") + \
               s[i:i + k].count("o") + s[i:i + k].count("u")

        if calc > res:
            res = calc

    return res



if __name__ == '__main__':
    print(maxVowels("", 3))
