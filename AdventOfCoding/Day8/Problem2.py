from math import lcm


def read_file():
    with open(
        "/Users/fabianstiewe/Desktop/Coding/Github "
        "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day8/input1.txt",
        "r",
    ) as f:
        return f.read().splitlines()


def calc(lines):
    graph = dict()
    muster = lines[0]

    start_nodes = []

    for i in range(2, len(lines)):
        node = lines[i].split(" ")[0]
        if node.endswith("A"):
            start_nodes.append(node)

        node_t1 = (lines[i].split(" "))[2].replace("(", "").replace(",", "")
        node_t2 = (lines[i].split(" "))[-1].replace(")", "")

        graph.update({node: [node_t1, node_t2]})

    res = []
    print(start_nodes)
    for start in start_nodes:
        counter = 0
        curr_node = start
        while True:
            if muster[counter % len(muster)] == "L":
                ind = 0
            else:
                ind = 1

            curr_node = graph[curr_node][ind]
            counter += 1
            if curr_node.endswith("Z"):
                res.append(counter)
                break

    print(res)
    return lcm(*res)


if __name__ == "__main__":
    print(calc(read_file()))
