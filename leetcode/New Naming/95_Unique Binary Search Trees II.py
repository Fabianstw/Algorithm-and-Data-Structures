# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n, start=True):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        for i in range(1, n+1):
            head = TreeNode(i)
            for left in range(1, i):
                head.left = self.generateTrees(left, False)
            for right in range(i+1, n):
                head.right = self.generateTrees(right, False)
            return head



if __name__ == '__main__':
    c = Solution()
    a = c.generateTrees(3)
    print(a.right.val)