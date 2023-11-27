"""Zwei Algorithmen zu Spielerstatistiken auf einem Server"""

from random import randint


class Hashtable:

    def __init__(self, player_ids):
        # hash func -> h(k) = k mod 50000
        # self.hash_table_different = [[] for n in range(50000)]
        # self.__insert_different(player_ids)

        # hash func -> l(k) = k mod 2000
        self.hash_table_most_plays = [[] for n in range(500000)]
        self.most_plays = [None, 0]
        self.__insert_most_plays(player_ids)

    def __insert_different(self, player_ids):
        for player_id in player_ids:
            if not self.__search_different(player_id):
                self.hash_table_different[player_id % 50000].append(player_id)

    def __search_different(self, player_id):
        k = player_id % 50000
        if player_id in self.hash_table_different[k]:
            return True
        return False

    def different_players(self):
        result = 0
        for step in self.hash_table_different:
            result += len(step)
        return result

    def __insert_most_plays(self, player_ids):
        for i, player_id in enumerate(player_ids):
            k = player_id % 500000
            if not self.__search_most_plays(player_id):
                self.hash_table_most_plays[k].append([player_id, 1])
                if self.most_plays[0] is None:
                    self.most_plays = [player_id, 1]
            else:
                for j, player in enumerate(self.hash_table_most_plays[k]):
                    if player[0] == player_id:
                        self.hash_table_most_plays[k][j][1] += 1
                        if self.hash_table_most_plays[k][j][1] > self.most_plays[1]:
                            self.most_plays = self.hash_table_most_plays[k][j]

        print(self.hash_table_most_plays)

    def player_most_plays(self):
        return self.most_plays[0], self.most_plays[1]

    def __search_most_plays(self, player_id):
        k = player_id % 500000
        for current_values in self.hash_table_most_plays[k]:
            if player_id == current_values[0]:
                return True
        return False


if __name__ == '__main__':
    # 10000 Spieler
    player_ids_main = [randint(1000, 50000000) for _ in range(10000000)]
    print(player_ids_main)
    hashing = Hashtable(player_ids_main)
    most = hashing.player_most_plays()
    print(most)
    print(player_ids_main.count(most[0]))


