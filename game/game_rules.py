from operator import attrgetter
from random import randrange, shuffle

from models import *


def _tabletop_move(player, tabletop_size):
    position = player.position
    rolled_dice = randrange(1, 7)
    new_position = position + rolled_dice
    if new_position >= tabletop_size:
        new_position -= tabletop_size
        player.receive_money(100)
    player.set_position(new_position)
    return new_position


def buying_building(player, building):
    building.set_owner(player)


def _shuffle_players(players):
    shuffle(players)


def _pay_rent(owner_player, paying_player, value):
    if paying_player.wallet >= value:
        owner_player.receive_money(value)
        paying_player.pay(value)
    else:
        paying_player.bankruptcy()


def _start_tabletop():
    tabletop = [None]
    for _ in range(20):
        value = randrange(3, 8) * 10
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
        will_buy = player.will_buy(building.value)
        if will_buy:
            buying_building(player, building)
    elif owner != player:
        _pay_rent(owner, player, building.value)


def _show_winner(player_list):
    ranked = sorted(player_list, key=attrgetter("wallet"), reverse=True)
    print(ranked[0].name, "e o vencedor!")
    return ranked[0].name


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
    winner = _show_winner(all_players)
    return GameStatistics(winner, actual_round)


def start_games():
    max_rounds = 1000
    max_games = 2

    player1 = ImpulsivePlayer('Impulsivo')
    player2 = DemandingPlayer('Exigente')
    player3 = CautiousPlayer('Cuidadoso')
    player4 = RandomPlayer('Aleatorio')

    all_players = [player1, player2, player3, player4]
    game_results = []

    for game in range(max_games):
        game_result = _single_game(all_players[:], max_rounds)
        game_results.append(game_result)
        for player in all_players:
            player.reset_player()
    return game_results
