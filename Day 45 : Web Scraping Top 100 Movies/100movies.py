from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

with open("movies.txt", "w") as movies :
    for movie in reversed(movie_tags):
        movie_title = movie.getText()
        movies.write(movie_title + "\n")
