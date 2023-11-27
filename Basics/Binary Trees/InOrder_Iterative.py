"""Inorder Iterative Traversal of a Binary Tree"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder_iterative(node):
    result = []
    stack = []
    current_node = node
    while True:
        if current_node is not None:
            stack.append(current_node)
            current_node = current_node.left
        elif stack:
            current_node = stack.pop()
            result.append(current_node.key)
            current_node = current_node.right
        else:
            break

    return result


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(inorder_iterative(root))
