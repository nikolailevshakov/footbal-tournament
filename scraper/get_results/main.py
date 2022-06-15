import urllib.request, ast
from getPredictions import get_predictions
import props
from Game import Game
from getResults import get_results
from calcPoints import calc_points


# get top_games from get_games
top_games_str = urllib.request.urlopen(props.top_games_url).read().decode('utf-8')
print("Get this string --->", top_games_str)

# turn to dictionary
top_games_dict = ast.literal_eval(top_games_str)
top_games = []

# convert string to Game object
for day in top_games_dict.keys():
    for game_string in top_games_dict[day]:
        time = game_string.split(",")[0]
        team_1 = game_string.split(",")[1]
        team_2 = game_string.split(",")[2]
        top_games.append(Game(day, time, team_1, team_2))

for g in top_games:
    g.desc()

# get results
all_games_results = get_results()
print(len(all_games_results))

#for g in all_games_results:
#    g.desc()

for g in top_games:
    for g_res in all_games_results:
        if g.team_1 == g_res.team_1 and g.team_2 == g_res.team_2:
            g.set_result(g_res.result)

# add top games results to one array
top_games_results = []
for g in top_games:
    g.desc()
    top_games_results.append(g.result)

for result in top_games_results:
    print(result)

game_predictions_dict = get_predictions()

name_points_dict = {}
for name in game_predictions_dict.keys():
    name_points_dict[name] = calc_points(game_predictions_dict[name], top_games_results)