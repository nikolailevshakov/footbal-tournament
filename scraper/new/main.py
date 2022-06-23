import requests
from bs4 import BeautifulSoup

URL = "https://www.flashscore.com/football/england/premier-league/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="fsbody")

print(results.encode("utf-8"))