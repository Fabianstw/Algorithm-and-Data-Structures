import math


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        options = coins
        res = [0]
        for i in range(1, amount + 1):
            res.append(-1)
            for option in options:
                if i - option == 0:
                    res[i] = 1
                    break
                if i - option > 0:
                    if res[i - option] > 0:
                        if res[i] == -1:
                            res[i] = res[i - option] + 1
                        elif res[i] > 1 + res[i - option]:
                            res[i] = res[i - option] + 1

        return res[len(res) - 1]


if __name__ == '__main__':
    c = Solution()
    print(c.coinChange([186,419,83,408], 6249))
