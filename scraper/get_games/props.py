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

days_before_saturday = 1
days_before_sunday = 2
calender = '/fixtures/'
table = '/standings/'
path_to_driver = str(pathlib.Path(__file__).parent.resolve())[:-9] + "\geckodriver.exe"

top_teams = ['Тоттенхэм', 'Манчестер Юнайтед', 'Челси', 'Ливерпуль', 'Манчестер Сити', 'Арсенал', 'Лестер'
             'Бавария', 'Боруссия Д', 'Байер', 'РБ Лейпциг',
             'Барселона', 'Реал Мадрид', 'Атлетико', 'Валенсия', 'Севилья'
             'Ювентус', 'Милан', 'Аталанта', 'Наполи', 'Рома', 'Лацио', 'Интер',
             'Зенит', 'ЦСКА', 'Спартак Москва', 'Локомотив Москва', 'Краснодар', 'Динамо Москва',
             'ПСЖ', 'Монако', 'Марсель', 'Лион', 'Лилль']

raitings = {}