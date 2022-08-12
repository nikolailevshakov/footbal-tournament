import props
from gameFunctions import collect_games, sort_games
from datetime import date
from raiting import get_teams_raitings
import json
import datetime

today_date = date.today()

# saturday = "13.08.2022"
# sunday = "14.08.2022"
# get next saturday and sunday based on the today's date
today = datetime.date.today()
saturday = today + datetime.timedelta((5-today.weekday()) % 7)
sunday = today + datetime.timedelta((6-today.weekday()) % 7)
saturday = saturday.strftime("%d.%m.%Y")
sunday = sunday.strftime("%d.%m.%Y")

weekend = [saturday, sunday]

all_games = []
for url_league in props.leagues:
    get_teams_raitings(url_league)
    all_games += collect_games(url_league, weekend)

gs = sort_games(all_games)


with open('../top_games.txt', 'w',  encoding='utf-8') as f:
    for g in gs:
        # {"date": "07.08.2022", "time": "17:30", "team_1": "Вест Хэм", "team_2": "Манчестер Сити", "score": 42}
        json.dump(g.__dict__, f, ensure_ascii=False)
        f.write('\n')


