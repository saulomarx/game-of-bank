# Quantas partidas terminam por time out (1000 rodadas); Done
#
# Quantos turnos em média demora uma partida; done
#
# Qual a porcentagem de vitórias por comportamento dos jogadores;
#
# Qual o comportamento que mais vence.
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
    print("Numero de jogos com timeout:", timeout_count)
    print("Duracao media de rounds:", avg_rounds)
