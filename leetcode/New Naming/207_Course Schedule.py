class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        grid = {course: [] for course in range(numCourses)}
        print(grid)
        for pre in prerequisites:
            current = grid.get(pre[1])
            current.append(pre[0])
            grid.update({pre[1]: current})

        for pre in prerequisites:
            visited = set()
            queue = [pre[0]]
            while queue:
                curr_queue = queue
                queue = []
                for curr_node in curr_queue:
                    if curr_node in visited:
                        return False
                    visited.add(curr_node)
                    for neighbour in grid[curr_node]:
                        queue.append(neighbour)

        return True



if __name__ == '__main__':
    c = Solution()
    print(c.canFinish(2, [[1,0],[0,1]]))