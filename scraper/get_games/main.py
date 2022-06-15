import props
from flask import Flask
from selenium.webdriver import Firefox
from gameFunctions import collect_games, sort_games, export_games

from datetime import date

today_date = date.today()
print(props.path_to_driver)
driver = Firefox(executable_path=props.path_to_driver)

all_games = collect_games(driver)
print("Number of all games: ", len(all_games))
if len(all_games)>10:
    top_games = sort_games(all_games)
    print("Number of top games: ", len(top_games))
    for g in top_games:
        g.desc()
else:
    print("ERROR: Less than 10 games")
    print("=========================")

driver.quit()

top_games_dict = export_games(top_games)
print(top_games_dict)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/top_games')
def index():
    return top_games_dict


if __name__ == "__main__":
    app.run()
