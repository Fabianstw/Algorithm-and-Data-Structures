# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        in_order_list = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            in_order_list.append(node.val)
            inorder(node.right)

        inorder(root)
        for i in range(1, len(in_order_list)):
            if in_order_list[i] <= in_order_list[i-1]:
                return False
        return True


if __name__ == '__main__':
    # [5,1,4,null,null,3,6] as tree
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    c = Solution()
    print(c.isValidBST(root))