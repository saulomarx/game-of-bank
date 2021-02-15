import random
from models import Building


def _roll_dice():
    return random.randrange(1, 6)


def _shuffle_players(players):
    random.shuffle(players)


def _pay_rent(owner_player, paying_player, value):
    owner_player.wallet = owner_player.wallet - value
    paying_player.wallet = paying_player.wallet + value


def _start_tabletop():
    tabletop = [None]
    for _ in range(20):
        value = random.randrange(3, 7) * 10
        building = Building(value)
        tabletop.append(building)
    return tabletop


def _game():
    print("Start game")


if __name__ == "__main__":
    _game()
