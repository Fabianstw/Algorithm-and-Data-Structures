class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        letter_list = [i for i in 'abcdefghijklmnopqrstuvwxyz']
        if endWord not in wordList:
            return 0
        queue = [beginWord]
        counter = 0
        visited = {}
        while queue:
            curr_queue = queue
            queue = []
            counter += 1
            for node in curr_queue:
                for letter in letter_list:
                    for i in range(len(beginWord)):
                        string_list = list(node)
                        string_list[i] = letter
                        word = ''.join(string_list)
                        if word in wordList:
                            if word == endWord:
                                return counter
                            if word not in visited:
                                visited.update({word: counter})
                                queue.append(word)
        return 0

    def change_second_char(self, word, new_char, position):
        # Convert the string to a list
        string_list = list(word)

        # Change the second character
        string_list[position] = new_char

        # Convert the list back to a string
        modified_string = ''.join(string_list)

        return modified_string



if __name__ == '__main__':
    c = Solution()
    c.ladderLength("a", "asudhj", [])