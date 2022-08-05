from readGames import read_games, write_scores, read_predictions
import props
from getResults import get_league_results
from calcPoints import calc_points


# read chosen games from the txt file
games_read = read_games()

# get results
all_games_results = []
for league in props.leagues:
    all_games_results += get_league_results(league, games_read)
# print(len(all_games_results))

for game_result in all_games_results:
    print(game_result)

# set results to games
for game in games_read:
    for game_res in all_games_results:
        if game.team_1 == game_res.team_1 and game.team_2 == game_res.team_2:
            game.set_result(game_res.result)

# list of games results
top_games_results = []
for game in games_read:
    top_games_results.append(game.result)

# get predictions from users -> dict[player_name] = list[game_prediction, ...]
players_predictions = read_predictions()

# get dict of name=score for each player
name_points_dict = {}
for name in players_predictions.keys():
    name_points_dict[name] = calc_points(players_predictions[name], top_games_results)

write_scores(name_points_dict)