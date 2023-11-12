"""Find a permutation of a string in another string"""

from itertools import permutations


def checkInclusion(s1: str, s2: str) -> bool:

    for i in range(len(s2) - len(s1) + 1):
        current_str = s2[i:i+len(s1)]
        i = 0
        cur_set = set()
        for char in current_str:
            if char not in cur_set:
                cur_set.add(char)
                if current_str.count(char) != s1.count(char):
                    break
                else:
                    i += 1
                    if i == len(s1):
                        return True

    return False



if __name__ == '__main__':
    print(checkInclusion("ab",
                         "eidboaoo"))
