"""Zombieinvaison"""


class ZombieInvasion:

    def __init__(self, k):
        # create a k * k graph alle node are connected verticly and horizontaly
        self.graph = {x: [] for x in range(k * k)}

    def remove_wall(self, row, col):
        position = col-1 + col * (row-1)
        # add the neighbours of position to position
        if position + 1 < len(self.graph):
            self.graph[position].append(position + 1)
        if position - 1 > 0:
            self.graph[position].append(position - 1)
        if position + 6 < len(self.graph):
            self.graph[position].append(position + 6)
        if position - 6 > 0:
            self.graph[position].append(position - 6)

    def print(self):
        # print line for line
        for i in range(len(self.graph)):
            try:
                print(i, ": ", self.graph[i])
            except KeyError:
                pass


if __name__ == '__main__':
    zi = ZombieInvasion(6)
    # zi.print()
    #testcases
    zi.remove_wall(2, 4)
    zi.print()

