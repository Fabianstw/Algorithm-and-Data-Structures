"""Reverse the binary tree"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverse_tree(node):
    if node is None:
        return

    new_root = Tree(node.data)
    new_root.left = reverse_tree(node.right)
    new_root.right = reverse_tree(node.left)
    return new_root


if __name__ == '__main__':
    root = Tree(5)
    root.left = Tree(3)
    root.right = Tree(10)
    root.left.left = Tree(2)
    root.left.right = Tree(4)
    root.right.left = Tree(7)
    root.right.right = Tree(15)

    c = reverse_tree(root)
    print(c.data)
    print(c.left.data)
    print(c.right.data)
    print(c.left.left.data)
    print(c.left.right.data)
    print(c.right.left.data)
    print(c.right.right.data)

