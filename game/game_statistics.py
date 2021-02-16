# Quantas partidas terminam por time out (1000 rodadas); Done
#
# Quantos turnos em média demora uma partida;
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


def show_game_data(game_results, max_rounds):
    timeout_count = _count_timeout(game_results, max_rounds)
    print(timeout_count)
