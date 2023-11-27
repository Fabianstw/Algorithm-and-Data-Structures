"""Aufgabe Betriebsfeier Algo Blatt 13"""
import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.factor = -99999


def print_tree(node, level=0):
    if node is None:
        return
    print("  " * level + str(node.value))
    if node.children:
        for child in node.children:
            print_tree(child, level + 1)


def post_order(node):
    if node is None:
        return
    for children in node.children:
        post_order(children)
    print(node.value)


def get_factor(node):
    skipv = 0
    for children in node.children:
        skipv += get_factor(children)

    keepv = node.value
    for children in node.children:
        for grandchild in children.children:
            keepv += grandchild.factor

    node.factor = max(skipv, keepv)
    return node.factor


if __name__ == '__main__':
    # create a treeNode
    tree = TreeNode(10)
    tree.children = [TreeNode(1), TreeNode(5)]
    tree.children[0].children = [TreeNode(-9), TreeNode(5), TreeNode(8)]
    tree.children[1].children = [TreeNode(-7), TreeNode(2)]
    tree.children[0].children[1].children = [TreeNode(-1), TreeNode(5), TreeNode(-9)]
    tree.children[1].children[1].children = [TreeNode(-9), TreeNode(9)]

    print(get_factor(tree))
