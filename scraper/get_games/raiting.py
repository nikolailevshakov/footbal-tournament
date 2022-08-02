import props
from bs4 import BeautifulSoup
import requests


def get_teams_raitings(league_path: str) -> None:
    r = requests.get(league_path+props.table)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find("div", class_="table-responsive")
    teams = []
    for team in table.find_all("td", class_="name left"):
        teams.append(team.text)

    for i, team in enumerate(teams):
        score = len(teams) - i
        if team in props.top_teams:
            score += 5
        props.raitings[team] = score
    print(league_path, " teams raitings is done!")
