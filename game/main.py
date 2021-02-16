from game_rules import start_games
from game_statistics import show_game_data


if __name__ == "__main__":
    max_rounds = 1000
    max_games = 2

    game_results = start_games(max_rounds, max_games)
    show_game_data(game_results, max_rounds)
