from collections import Counter


def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github "
              "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day7/input1.txt", "r") as f:
        return f.read().splitlines()


def calc(lines):
    tmp = [[], [], [], [], [], [], []]
    for line_com in lines:
        # print(line_com)
        hand, bid = line_com.split(" ")
        scored_hand = Counter(hand)
        # high card
        if len(scored_hand) == 1:
            tmp[0].append([hand, bid])
            continue
        else:
            if "J" in scored_hand.keys():
                Js = scored_hand.pop("J")
                while Js > 0:
                    # get the key with the highest value
                    max_key = max(scored_hand, key=scored_hand.get)
                    scored_hand[max_key] += 1
                    Js -= 1

        # full cards
        if len(scored_hand) == 1:
            tmp[0].append([hand, bid])

        elif len(scored_hand) == 4:
            tmp[5].append([hand, bid])

        # two pair, three of a kind
        elif len(scored_hand) == 3:
            if 3 not in scored_hand.values():
                tmp[4].append([hand, bid])

            else:
                tmp[3].append([hand, bid])

        # full house, four of a kind
        elif len(scored_hand) == 2:
            if 4 not in scored_hand.values():
                tmp[2].append([hand, bid])

            else:
                tmp[1].append([hand, bid])

        # one of a kind
        else:
            tmp[6].append([hand, bid])

    res = []
    for tm in tmp:
        for i in range(len(tm)):
            for j in range(0, len(tm) - 1):
                if compareString(tm[j][0], tm[j + 1][0]):
                    tm[j], tm[j + 1] = tm[j + 1], tm[j]
        for t in tm:
            res.append(t)

    print(len(res))

    ans = 0
    for i in range(len(res)):
        # print((len(res)-i), int(res[i][1]), res[i][0])
        ans += (len(res) - i) * int(res[i][1])

    return ans


def compareString(s1, s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:
            return "AKQT98765432J".index(s1[i]) > "AKQT98765432J".index(s2[i])


if __name__ == '__main__':
    lines = read_file()
    print(calc(lines))

    # 350650319 to high
    # 254083736 correct
    # 253948807 to low
