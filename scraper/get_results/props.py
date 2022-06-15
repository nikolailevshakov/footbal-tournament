import pathlib
url_main = 'https://www.flashscore.ru/'
url_england = 'https://www.flashscore.ru/football/england/premier-league'
url_france = "https://www.flashscore.ru/football/france/ligue-1"
url_germany = "https://www.flashscore.ru/football/germany/bundesliga"
url_spain = "https://www.flashscore.ru/football/spain/laliga"
url_italy = "https://www.flashscore.ru/football/italy/serie-a"
url_russia = "https://www.flashscore.ru/football/russia/premier-league"
url_champions = "https://www.flashscore.ru/football/europe/champions-league"
url_europe = "https://www.flashscore.ru/football/europe/europa-league"

leagues = [url_england, url_france, url_germany, url_spain, url_italy, url_russia]

top_games_url = "http://localhost:5000/top_games"
predictions_url = "http://localhost:5001/predictions"

results = "/results/"

path_to_driver = str(pathlib.Path(__file__).parent.resolve())[:-11] + "\geckodriver.exe"