import props
from gameFunctions import collect_games, sort_games, export_games
from datetime import date
from raiting import get_teams_raitings

today_date = date.today()


#get_teams_raitings(props.url_england)
collect_games()

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

