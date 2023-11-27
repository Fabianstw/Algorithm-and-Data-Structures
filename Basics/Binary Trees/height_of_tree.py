
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def calc_height(root):
    if root is None:
        return 0
    return 1 + max(calc_height(root.left), calc_height(root.right))


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.left = TreeNode(5)
    root1.left.left.right = TreeNode(6)
    root1.left.left.right.left = TreeNode(7)

    print(calc_height(root1))
