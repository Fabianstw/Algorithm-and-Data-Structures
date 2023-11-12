# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def helper(node, height):
            if node is None:
                return
            if height > len(result) - 1:
                result.append([node.val])
            else:
                result[height].append(node.val)

            helper(node.left, height+1)
            helper(node.right, height+1)

        helper(root, 0)
        return result


if __name__ == '__main__':
    # [3,9,20,null,null,15,7] as tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    c = Solution()
    print(c.levelOrder(root))