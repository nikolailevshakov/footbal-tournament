import ast
import urllib.request

import props

# getting predictions as a dictionary of name:
# array of results in the same order as it was received from get_games
def get_predictions():
    game_predictions = urllib.request.urlopen(props.predictions_url).read().decode('utf-8')
    print("Get this predictions --->", game_predictions)

    game_predictions_dict = ast.literal_eval(game_predictions)

    # get dictionary with array of results as a value and name as a key
    for name in game_predictions_dict.keys():
        game_predictions_dict[name] = ast.literal_eval(game_predictions_dict[name])
    return game_predictions_dict