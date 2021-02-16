import random
from models import *


def _roll_dice():
    # TODO CHANGE HERE!
    return random.randrange(1, 3)


def _tabletop_move(player, tabletop_size):
    position = player.position
    rolled_dice = _roll_dice()
    new_position = position + rolled_dice
    if new_position >= tabletop_size:
        new_position -= tabletop_size
        player.receive_money(100)
    player.set_position(new_position)
    return new_position


def buying_building(player, building):
    building.set_owner(player)


def _shuffle_players(players):
    random.shuffle(players)


def _pay_rent(owner_player, paying_player, value):
    if paying_player.wallet >= value:
        owner_player.receive_money(value)
        paying_player.pay(value)
    else:
        paying_player.bankruptcy()


def _start_tabletop():
    tabletop = [None]
    for _ in range(20):
        value = random.randrange(3, 8) * 10
        building = Building(value)
        tabletop.append(building)
    return tabletop


def _remove_bankrupt_player(tabletop, player):
    for building in tabletop[1:]:
        if building.owner == player:
            building.remove_owner()


def _buy_or_pay(player, building):
    owner = building.owner

    if owner is None:
        print(player.name)
        will_buy = player.will_buy(building.value)
        if will_buy:
            print("Comprando")
            buying_building(player, building)
        else:
            print("Nao compra")
    elif owner != player:
        print("paga")
        _pay_rent(owner, player, building.value)
    else:
        pass


def _game():
    max_rounds = 100

    player1 = ImpulsivePlayer('Impulsivo')
    player2 = DemandingPlayer('Exigente')
    player3 = CautiousPlayer('Cuidadoso')
    player4 = RandomPlayer('Aleatorio')

    all_players = [player1, player2, player3, player4]
    _shuffle_players(all_players)

    table_top = _start_tabletop()
    table_top_size = len(table_top)

    for round in range(max_rounds):
        for player in all_players:
            if player.wallet > 0:
                player_position = _tabletop_move(player, table_top_size)
                if player_position != 0:
                    _buy_or_pay(player, table_top[player_position])
                if player.wallet == 0:
                    print("faliu")


if __name__ == "__main__":
    _game()
