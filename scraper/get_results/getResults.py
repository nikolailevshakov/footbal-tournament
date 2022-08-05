import bs4.element
from Game import Game
import props, requests
from bs4 import BeautifulSoup
from GameResult import GameResult


def get_league_results(league_url: str, games: list[Game]) -> list[GameResult]:
    r = requests.get(league_url + props.results)
    soup = BeautifulSoup(r.text, 'html.parser')
    matches_list = soup.find("div", class_="matches-list")
    dates = matches_list.find_all("div", class_="matches-list-date")
    games_results = []
    for date in dates:
        for g in games:
            if g.date in dates:
                while True:
                    if isinstance(date.next_sibling, bs4.element.NavigableString):
                        date = date.next_sibling
                        continue
                    if date.next_sibling.attrs['class'] == ['matches-list-date']:
                        break
                    game_result = create_game_result(date.next_sibling, g.team_1, g.team_2)
                    games_results.append(game_result)
                    date = date.next_sibling
    return games_results


def create_game_result(game_tag: bs4.element.Tag, team_1: str, team_2: str) -> GameResult:
    score = game_tag.find("span", class_="score has-score").text.strip().replace(':', '')
    return GameResult(team_1, team_2, score)