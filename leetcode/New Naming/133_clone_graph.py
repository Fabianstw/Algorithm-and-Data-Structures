
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        queue = [node]
        created_list = [0 for _ in range(101)]
        visited = set()
        while len(queue) > 0:
            curr_queue = queue
            queue = []
            for curr_node in curr_queue:
                if curr_node not in visited:
                    visited.add(curr_node)
                    if created_list[curr_node.val] == 0:
                        new_node = Node(curr_node.val)
                        created_list[curr_node.val] = new_node
                    for neighbours in curr_node.neighbors:
                        queue.append(neighbours)
                        if created_list[neighbours.val] == 0:
                            new_node = Node(neighbours.val)
                            created_list[neighbours.val] = new_node

                        created_list[curr_node.val].neighbors.append(created_list[neighbours.val])

        return created_list[node.val]

if __name__ == '__main__':
    c = Solution()
    # create this graoh[[2, 4], [1, 3], [2, 4], [1, 3]]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print(c.cloneGraph(node1))
