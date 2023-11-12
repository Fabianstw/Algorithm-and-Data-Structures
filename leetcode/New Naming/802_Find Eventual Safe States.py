class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        res = set()
        while True:
            added = False
            for node in range(len(graph)):
                if len(graph[node]) == 0:
                    added = True
                    res.add(node)
                    graph[node] = [-1]
                else:
                    included = True
                    for value in graph[node]:
                        if value not in res:
                            included = False
                            break
                    if included:
                        added = True
                        res.add(node)
                        graph[node] = [-1]

            if added is False:
                res = list(res)
                res.sort()
                return res


if __name__ == '__main__':
    c = Solution()
    print(c.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))