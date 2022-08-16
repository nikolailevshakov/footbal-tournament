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
        starting_date = date
        for g in games:
            date = starting_date
            if isinstance(date, bs4.element.NavigableString): continue
            if g.date != date.text: continue
            while True:
                if isinstance(date.next_sibling, bs4.element.NavigableString):
                    date = date.next_sibling
                    continue
                if date.next_sibling is None:
                    break
                if date.next_sibling.attrs['class'] == ['matches-list-date']:
                    break
                team_1 = date.next_sibling.find("span", class_="team team1").text.strip()
                team_2 = date.next_sibling.find("span", class_="team team2").text.strip()
                if g.team_1 == team_1 and g.team_2 == team_2:
                    game_result = create_game_result(date.next_sibling, g.team_1, g.team_2)
                    games_results.append(game_result)
                date = date.next_sibling
    return games_results


def create_game_result(game_tag: bs4.element.Tag, team_1: str, team_2: str) -> GameResult:
    score = game_tag.find("span", class_="score has-score").text.strip().replace(':', '')
    return GameResult(team_1, team_2, score)