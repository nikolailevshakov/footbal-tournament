from datetime import date, datetime, timedelta
from Game import Game
import props, requests
from bs4 import BeautifulSoup
from raiting import get_teams_raitings

saturday = "06.08.2022"
sunday = "07.08.2022"
weekend = [saturday, sunday]

# collect game divs into the array
def collect_games():
    r = requests.get(props.url_russia + props.calender)
    soup = BeautifulSoup(r.text, 'html.parser')
    matches_list = soup.find("div", class_="matches-list")
    dates = matches_list.find_all("div", class_="matches-list-date")
    for date in dates:
        if date.text in weekend:
            while date.next_sibling == ' ': date = date.next_sibling
            while 'href' in date.next_sibling.attrs.keys():
                print(date.next_sibling.text)
                date = date.next_sibling
            while date.next_sibling == ' ': date = date.next_sibling



    # for league_path in props.leagues:
    #     driver.get(league_path)
    #     driver.implicitly_wait(10)
    #     div_games = driver.find_elements_by_class_name("event__match")
    #     games = filter(None, [create_game(div_game) for div_game in div_games])
    #     get_teams_raitings(league_path, driver)
    #     for game in games:
    #         game.set_score()
    #         all_games.append(game)
    #         print(game.desc())
    # return all_games


# Parse div of the game in to the object Game
def create_game(div_game):
    div_game_arr = div_game.text.split("\n")
    game_date = str(date.today().year)[2:]+"."+div_game_arr[0].split(" ")[0]
    game_date_format = datetime.strptime(game_date, '%y.%d.%m.').date()
    time = div_game_arr[0].split(" ")[1]
    team_1 = div_game_arr[1]
    team_2 = div_game_arr[2]
    if game_date_format.weekday() == 5:
        game_date = "Суббота"
        return Game(game_date, time, team_1, team_2)

    if game_date_format.weekday() == 6:
        game_date = "Воскресенье"
        return Game(game_date, time, team_1, team_2)


def sort_games(all_games):
    top_games = []
    scores = []
    for game in all_games:
        scores.append(game.score)
    while len(top_games) != 10:
        max_score = max(scores)
        print(max_score, len(scores))
        for game in all_games:
            if game.score == max_score:
                top_games.append(game)
                all_games.remove(game)
                scores.remove(max_score)
                break
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