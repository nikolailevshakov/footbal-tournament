import props
from gameFunctions import collect_games, sort_games
from datetime import date
from raiting import get_teams_raitings

today_date = date.today()

saturday = "06.08.2022"
sunday = "07.08.2022"
weekend = [saturday, sunday]

all_games = []
for url_league in props.leagues:
    get_teams_raitings(url_league)
    all_games += collect_games(url_league, weekend)
gs = sort_games(all_games)
for g in gs: print(g)
#
# all_games = collect_games(driver)
#
# if len(all_games)>10:
#     top_games = sort_games(all_games)
#     print("----INFO Number of top games: ", len(top_games))
#     for g in top_games:
#         g.desc()
# else:
#     print("----ERROR: Less than 10 games")
#     print("=========================")
#
# driver.quit()
#
# top_games_dict = export_games(top_games)

