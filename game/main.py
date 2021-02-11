import random


def roll_dice():
    return random.randrange(1, 6)


def shuffle_players(players):
    random.shuffle(players)

