"""Group anagrams in a list"""

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) < 2:
        return [strs]
    res = dict()
    tmp = set()
    for i in range(len(strs)):
        sorted_s = "".join(sorted(strs[i]))
        if sorted_s in tmp:
            res[sorted_s].append(strs[i])
        else:
            res[sorted_s] = [strs[i]]
            tmp.add(sorted_s)

    return list(res.values())


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen = set()
    for i in range(len(s)):
        if s[i] not in seen:
            if s.count(s[i]) != t.count(s[i]):
                return False
            seen.add(s[i])
    return True


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
