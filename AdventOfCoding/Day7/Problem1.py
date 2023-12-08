from collections import Counter

def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github "
              "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day7/input1.txt", "r") as f:
        return f.read().splitlines()




def calc (lines):
    tmp = [[], [], [], [], [], [], []]
    for line_com in lines:
        hand, bid = line_com.split(" ")
        scored_hand = Counter(hand)

        # high card
        if len(scored_hand) == 5:
            tmp[6].append([hand, bid])
            print(tmp[6])

        # one pair
        elif len(scored_hand) == 4:
            tmp[5].append([hand, bid])
            print(tmp[5])

        # two pair, three of a kind
        elif len(scored_hand) == 3:
            if 3 not in scored_hand.values():
                tmp[4].append([hand, bid])
                print(tmp[4])
            else:
                tmp[3].append([hand, bid])
                print(tmp[3])

        # full house, four of a kind
        elif len(scored_hand) == 2:
            if 4 not in scored_hand.values():
                tmp[2].append([hand, bid])
                print(tmp[2])
            else:
                tmp[1].append([hand, bid])
                print(tmp[1])

        # five of a kind
        else:
            tmp[0].append([hand, bid])
            print(tmp[0])




    res = []
    for tm in tmp:
        for i in range(len(tm)):
            for j in range(0, len(tm)-1):
                if compareString(tm[j][0], tm[j+1][0]):
                    tm[j], tm[j+1] = tm[j+1], tm[j]
        for t in tm:

            res.append(t)

    print(res)

    ans = 0
    for i in range(len(res)):
        # print((len(res)-i), int(res[i][1]), res[i][0])
        ans += (len(res)-i) * int(res[i][1])

    return ans


def compareString(s1, s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:
            return "AKQJT98765432".index(s1[i]) > "AKQJT98765432".index(s2[i])


if __name__ == '__main__':
    lines = read_file()
    print(calc(lines))

    # 254365496 to high
    # 253962874 to high
    # 253910319 correct
    # 253038656 to low