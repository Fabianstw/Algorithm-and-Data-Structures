def calc():
    counter = 0
    band = ""
    init = []
    acc = []
    machine = {}

    while True:
        try:
            line = input()
            if line == "":
                continue
            if counter == 0:
                band = line.split(": ")[1].split(",")
            elif counter == 1:
                init = line.split(": ")[1].split(",")
            elif counter == 2:
                acc = line.split(": ")[1].split(",")
            else:
                line = line.split(",")
                sec = input().split(",")
                machine.update({(line[0], line[1]): (sec[0], sec[1], sec[2])})

            counter += 1
        except EOFError:
            break

    print(band)
    print(init)
    print(acc)
    print(machine)

    """
    Ab hier ist die Turingmaschine implementiert
    """

    index = 0

    curr_state = (init[0], band[index])
    while True:
        print(band)
        print(curr_state, index)
        if curr_state not in machine.keys():
            return band
        else:
            to_do = machine[curr_state]
            if 0 <= index < len(band):
                band[index] = to_do[1]
            elif index < 0:
                band.insert(0, to_do[1])
                index += 1
            elif index >= len(band):
                band.append(to_do[1])
            if to_do[2] == ">":
                index += 1
            elif to_do[2] == "<":
                index -= 1

            if index < 0 or index > len(band) - 1:
                curr_state = (to_do[0], "_")
            else:
                curr_state = (to_do[0], band[index])


if __name__ == "__main__":
    res = ""
    for i in calc():
        if i != "_":
            res += i + ","

    res = res[:len(res)-1]
    print(res)
