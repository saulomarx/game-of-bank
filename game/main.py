import random
import operator

from models import *


def _roll_dice():
    return random.randrange(1, 7)


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
            buying_building(player, building)
    elif owner != player:
        _pay_rent(owner, player, building.value)


def _show_winner(player_list):
    ranked = sorted(player_list, key=operator.attrgetter("wallet"), reverse=True)
    print(ranked[0].name, "e o vencedor!")


def _start_games():
    max_rounds = 1000
    max_games = 2

    player1 = ImpulsivePlayer('Impulsivo')
    player2 = DemandingPlayer('Exigente')
    player3 = CautiousPlayer('Cuidadoso')
    player4 = RandomPlayer('Aleatorio')

    all_players = [player1, player2, player3, player4]

    for game in range(max_games):
        _single_game(all_players[:], max_rounds)
        for player in all_players:
            player.reset_player()


def _single_game(all_players, max_rounds):
    _shuffle_players(all_players)

    tabletop = _start_tabletop()
    tabletop_size = len(tabletop)

    actual_round = 0
    while actual_round < max_rounds and len(all_players) > 1:
        actual_round += 1
        for player in all_players:
            player_position = _tabletop_move(player, tabletop_size)
            if player_position != 0:
                _buy_or_pay(player, tabletop[player_position])
            if player.wallet == 0:
                _remove_bankrupt_player(tabletop, player)
                all_players.remove(player)
    _show_winner(all_players)


if __name__ == "__main__":
    _start_games()
