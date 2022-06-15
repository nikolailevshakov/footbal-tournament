from datetime import date, datetime, timedelta
from Game import Game
import props
from Raiting import get_raitings


def create_game(div_game):
    div_game_arr = div_game.text.split("\n")
    game_date = str(date.today().year)[2:]+"."+div_game_arr[0].split(" ")[0]
    game_date_format = datetime.strptime(game_date, '%y.%d.%m.').date()
    time = div_game_arr[0].split(" ")[1]
    team_1 = div_game_arr[1]
    team_2 = div_game_arr[2]
    if game_date_format == date.today() + timedelta(props.days_before_saturday):
        game_date = "Суббота"
        return Game(game_date, time, team_1, team_2)

    if game_date_format == date.today() + timedelta(props.days_before_sunday):
        game_date = "Воскресенье"
        return Game(game_date, time, team_1, team_2)


def collect_games(driver):
    all_games = []
    for league_path in props.leagues:
        driver.get(league_path + props.calender)
        driver.implicitly_wait(5)
        div_games = driver.find_elements_by_class_name("event__match")

        games = filter(None, [create_game(div_game) for div_game in div_games])
        get_raitings(league_path, driver)
        for game in games:
            game.set_score()
            all_games.append(game)
    return all_games


def sort_games(all_games):
    top_games = []
    scores = []

    for game in all_games:
        scores.append(game.score)
    while len(top_games) != 10:
        max_score = max(scores)
        for game in all_games:
            if game.score == max_score:
                top_games.append(game)
                all_games.remove(game)
                scores.remove(max_score)
    return top_games


def export_games(top_games):
    sat_games = []
    sun_games = []
    for game in top_games:
        if game.date == "Суббота":
            sat_games.append(game)
        if game.date == "Воскресенье":
            sun_games.append(game)
    json_dict = {"Суббота": [game.serialize() for game in sat_games],
                 "Воскресенье": [game.serialize() for game in sun_games]}
    return json_dict