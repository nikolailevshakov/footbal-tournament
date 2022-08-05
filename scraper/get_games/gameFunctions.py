import bs4.element
from Game import Game
import props, requests
from bs4 import BeautifulSoup


# collect game divs into the array
def collect_games(league_url: str, days: list[str]) -> list[Game]:
    r = requests.get(league_url + props.calender)
    soup = BeautifulSoup(r.text, 'html.parser')
    matches_list = soup.find("div", class_="matches-list")
    dates = matches_list.find_all("div", class_="matches-list-date")
    games = []
    for date in dates:
        day_date = date.text
        if date.text in days:
            while True:
                if isinstance(date.next_sibling, bs4.element.NavigableString):
                    date = date.next_sibling
                    continue
                if date.next_sibling.attrs['class'] == ['matches-list-date']:
                    break
                games.append(create_game(date.next_sibling, day_date))
                date = date.next_sibling
    return games


def create_game(game_tag: bs4.element.Tag, day_date: str) -> Game:
    time = game_tag.find("span", class_="match-time-time").text.strip()
    team_1 = game_tag.find("span", class_="team team1").text.strip()
    team_2 = game_tag.find("span", class_="team team2").text.strip()
    return Game(day_date, time, team_1, team_2)


def sort_games(all_games: list[Game]) -> list[Game]:
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
                break
    return top_games