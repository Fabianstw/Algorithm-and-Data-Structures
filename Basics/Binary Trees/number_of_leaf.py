"""Calculate the number of leafs recursivly"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def calc_num_leafs(root):

    number_leafs = 0

    def calc_num_leafs_helper(root):
        if root is None:
            return
        if root.left is None and root.right is None:
            nonlocal number_leafs
            number_leafs += 1
        calc_num_leafs_helper(root.left)
        calc_num_leafs_helper(root.right)

    calc_num_leafs_helper(root)
    return number_leafs


if __name__ == '__main__':
    # create a tree with 5 leafs
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    root1.left.left.left = TreeNode(8)
    root1.left.left.right = TreeNode(9)
    root1.left.right.left = TreeNode(10)
    root1.left.right.right = TreeNode(11)
    root1.right.left.left = TreeNode(12)
    root1.right.left.right = TreeNode(13)
    root1.right.right.left = TreeNode(14)

    print(calc_num_leafs(root1))
