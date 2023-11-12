class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]

        if n < 1:
            return []

        res = set()
        for new_value in self.generateParenthesis(n - 1):
            res.add("()" + new_value)
            res.add("(" + new_value + ")")
            res.add(new_value + "()")

        for i in range(1, n-1):
            for new_value in self.generateParenthesis(i):
                for sec_value in self.generateParenthesis(n-i):
                    res.add(new_value+sec_value)

        return list(res)


if __name__ == '__main__':
    c = Solution()
    print(c.generateParenthesis(3))
