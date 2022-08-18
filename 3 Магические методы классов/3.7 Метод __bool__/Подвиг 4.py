import sys

class Player:
    def __init__(self, name, old, score):
        self.name, self.old, self.score = name, int(old), int(score)

    def __bool__(self):
        return self.score != 0

# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))


players = [Player(i.split(';')[0], i.split(';')[1], i.split(';')[2]) for i in lst_in if bool(Player(i.split(';')[0], i.split(';')[1], i.split(';')[2]))]
players_filtered = players[:]
