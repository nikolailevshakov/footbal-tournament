import json
from Game import Game
import os


def read_games() -> list[Game]:
    with open('../top_games.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    gs = []
    for line in lines:
        d_line = json.loads(line)
        gs.append(Game(d_line['date'], d_line['time'], d_line['team_1'], d_line['team_2']))
    return gs


def read_predictions() -> dict[str]:
    players_predictions = {}

    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    p = os.path.join(os.getcwd(), "players_preds")

    for filename in os.listdir(p):
        with open(os.path.join(p, filename), 'r') as f:
            predictions = f.readlines()
        predictions = [score.replace('\n', '') for score in predictions]
        players_predictions[filename.replace(".txt", "")] = predictions
    return players_predictions


# write scores to txt file
def write_scores(name_points_dict: dict[str]):
    with open('../player_scores.txt', 'w', encoding='utf-8') as f:
        for name, score in name_points_dict.items():
            f.write(name + " " + str(score))
            f.write('\n')
