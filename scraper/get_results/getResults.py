import props
from selenium.webdriver import Firefox
from gameResults import GameResult


def get_results():
    game_results = []
    driver = Firefox(executable_path=props.path_to_driver)
    for league_path in props.leagues:
        driver.get(league_path + props.results)
        driver.implicitly_wait(5)
        div_games = driver.find_elements_by_class_name("event__match")
        for div_game in div_games:
            team_1 = div_game.text.split("\n")[1]
            team_2 = div_game.text.split("\n")[2]
            result = div_game.text.split("\n")[3]+div_game.text.split("\n")[4]
            game_results.append(GameResult(team_1, team_2, result))
    driver.quit()
    return game_results
