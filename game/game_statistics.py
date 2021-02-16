def _show_best_player(rank):
    players_by_wins = {}
    players = rank.keys()

    for player in players:
        number_of_wins = rank[player]
        if number_of_wins in players_by_wins:
            players_by_wins[number_of_wins].append(player.name)
        else:
            players_by_wins[number_of_wins] = [player.name]

    players_scores = sorted(players_by_wins.keys(), reverse=True)
    best_score = players_scores[0]
    print("Jogador(es) com maior numero de vitorias:")
    for player in players_by_wins[best_score]:
        print(player)


def _show_win_rate(rank, number_of_games):
    players = rank.keys()
    for player in players:
        win_rate = rank[player] / number_of_games * 100
        print("Jogados", player.name, "->", win_rate, "%")


def _create_game_rank(game_results):
    rank = {}
    for result in game_results:
        if result.winner in rank:
            rank[result.winner] += 1
        else:
            rank[result.winner] = 1
    return rank


def _count_timeout(game_results, max_rounds):
    timeout_count = 0
    for result in game_results:
        if result.number_of_round == max_rounds:
            timeout_count += 1
    return timeout_count


def _avg_rounds(game_results):
    rounds_sum = 0
    for result in game_results:
        rounds_sum += result.number_of_round
    return rounds_sum / len(game_results)


def show_game_data(game_results, max_rounds):
    timeout_count = _count_timeout(game_results, max_rounds)
    avg_rounds = _avg_rounds(game_results)
    rank = _create_game_rank(game_results)

    print("Numero de jogos com timeout:", timeout_count)
    print("Duracao media de rounds:", avg_rounds)
    _show_win_rate(rank, len(game_results))
    _show_best_player(rank)
