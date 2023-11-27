"""Algo 1 Abgabe Blatt 12 Aufgabe 7"""


class Tree:

    def __init__(self, value):
        self.label = value
        self.parent = None
        self.left = None
        self.right = None


class Solution:

    def PrintTree(self, root):
        if root:
            print(root.label)
            self.PrintTree(root.left)
            self.PrintTree(root.right)

    def PrintTree2(self, root):
        if root:
            print(root.label)
            self.PrintTree2(root.right)
            self.PrintTree2(root.left)
        return

    def internal(self, root):
        result = []

        def getInterals(x):
            if x is None:
                return
            if x.left is not None or x.right is not None:
                result.append(x.label)
            getInterals(x.left)
            getInterals(x.right)

        getInterals(root)
        print(result)
        return result

    def r_path(self, root):
        if not root:
            return True
        if root.label == "R":
            if self.r_path(root.left):
                return True
            if self.r_path(root.right):
                return True
        return False



if __name__ == '__main__':
    node = Tree("R")
    node.left = Tree("R")
    node.right = Tree("R")
    node.right.left = Tree("R")
    node.right.right = Tree("L")
    node.right.right.right = Tree("k")

    c = Solution()
    c.PrintTree2(node)
    c.internal(node)
    print(c.r_path(node))

