from typing import List


class Solution:

    def get_next_bigger_element(self, lst, number):
        for element in lst:
            if element > number:
                return element
        return None
    def longestSubsequence_slow(self, arr: List[int], difference: int) -> int:
        cache = dict()
        for index, number in enumerate(arr):
            if number in cache:
                get_value = cache.get(number)
                get_value.append(index)
                cache.update({number: get_value})
            else:
                cache.update({number: [index]})

        visited = set()
        current_max = 0
        for index, number in enumerate(arr):
            if number not in visited:
                visited.add(number)
                new_max = 1
                current_value = number
                current_index = index
                while True:
                    if current_value + difference in cache:
                        all_index = cache.get(current_value + difference)
                        next_bigger = self.get_next_bigger_element(all_index, current_index)
                        if next_bigger:
                            current_index = next_bigger
                            new_max += 1
                            current_value += difference
                            visited.add(current_value)
                        else:
                            break
                    else:
                        break
                if new_max > current_max:
                    current_max = new_max
        return current_max

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        result = {}
        for num in arr:
            cache = num - difference
            if cache in result:
                result[num] = result[cache] + 1
            else:
                result[num] = 1

        return max(result.values())



if __name__ == '__main__':
    c = Solution()
    print(c.longestSubsequence([3,0,-3,4,-4,7,6], 3))