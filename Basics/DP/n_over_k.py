"""Abgabe zu n über k"""


class Solution:

    def rec_solution(self, n, k):
        if n == k or k == 0:
            return 1
        return self.rec_solution(n - 1, k - 1) + self.rec_solution(n - 1, k)

    def iter_shit_space(self, n, k):
        res_list = [[1 for _ in range(n+1)] for _ in range(k+1)]

        for i in range(k+1):
            # this one goes from top to bottom
            for j in range(0, n+1):
                if i - 1 >= 0 and j > i:
                    res_list[i][j] = res_list[i][j-1] + res_list[i-1][j-1]

        return res_list[len(res_list)-1][len(res_list[0]) - 1]

    def iter_better_spacce(self, n, k):
        list_0 = [1 for _ in range(n+1)]
        list_1 = [1 for _ in range(n+1)]

        for i in range(k+1):
            for j in range(n+1):
                if i-1 >= 0 and j > i:
                    if i % 2 == 0:
                        list_0[j] = list_0[j-1] + list_1[j-1]
                    else:
                        list_1[j] = list_1[j - 1] + list_0[j - 1]
            if i % 2 == 0:
                list_1 = [1 for _ in range(n+1)]
            else:
                list_0 = [1 for _ in range(n+1)]

        return max(max(list_1), max(list_0))


if __name__ == '__main__':
    c = Solution()
    print(c.iter_shit_space(20, 10))
    print(c.iter_better_spacce(20, 10))
