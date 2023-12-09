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
    print(muster)

    for i in range(2, len(lines)):
        node = lines[i].split(" ")[0]
        node_t1 = (lines[i].split(" "))[2].replace("(", "").replace(",", "")
        node_t2 = (lines[i].split(" "))[-1].replace(")", "")

        graph.update({node: [node_t1, node_t2]})

    counter = 0
    curr_node = "AAA"
    while True:
        if muster[counter % len(muster)] == "L":
            ind = 0
        else:
            ind = 1
        curr_node = graph[curr_node][ind]
        if curr_node == "ZZZ":
            return counter + 1
        counter += 1



if __name__ == "__main__":
    print(calc(read_file()))
