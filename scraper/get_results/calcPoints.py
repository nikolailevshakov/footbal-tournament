

def calc_points(game_preds, results):
    points = 0
    for i in range(len(game_preds)):
        if game_preds[i] == results[i]:
            points += 3
            continue
        if int(game_preds[i][0])-int(game_preds[i][1]) == int(results[i][0])-int(results[i][1]):
            points += 2
            continue
        if (int(game_preds[i][0])-int(game_preds[i][1])) > 0 and (int(results[i][0])-int(results[i][1])) > 0:
            points += 1
            continue
        if (int(game_preds[i][0]) - int(game_preds[i][1])) < 0 and (int(results[i][0]) - int(results[i][1])) < 0:
            points += 1
            continue
    return points
