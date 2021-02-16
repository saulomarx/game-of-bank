import random
from models import *


def _roll_dice():
    return random.randrange(1, 7)


def _tabletop_move(player, tabletop_size):
    position = player.position
    rolled_dice = _roll_dice()
    new_position = position + rolled_dice
    if new_position > tabletop_size:
        new_position -= tabletop_size


def _shuffle_players(players):
    random.shuffle(players)


def _pay_rent(owner_player, paying_player, value):
    owner_player.receive_money(value)
    paying_player.pay(value)


def _start_tabletop():
    tabletop = [None]
    for _ in range(20):
        value = random.randrange(3, 7) * 10
        building = Building(value)
        tabletop.append(building)
    return tabletop


def _game():
    max_rounds = 100

    player1 = ImpulsivePlayer()
    player2 = DemandingPlayer()
    player3 = CautiousPlayer()
    player4 = RandomPlayer()

    all_players = [player1, player2, player3, player4]
    _shuffle_players(all_players)

    table_top = _start_tabletop()

    for round in range(max_rounds):
        print(round+1)
        for player in all_players:
            print()


if __name__ == "__main__":
    _game()
