import requests
from bs4 import BeautifulSoup


response  = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

top_100_movie = response.text


soup = BeautifulSoup(top_100_movie, "html.parser")

h3_tag = soup.find_all("h3")
film_titles = [x.string for x in h3_tag ]
for x in reversed(film_titles):
    with open("top_100_film", "a",  encoding="utf-8") as top_100:
        top_100.write(f"\n{x}")