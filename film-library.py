import os
from datetime import date
import random

def cls():
    os.system('cls')

class Movie:
    def __init__(self, title, year, genre, views_nr):
        self.title = title
        self.year = year
        self.genre = genre
        self.views_nr = views_nr

    def __str__(self):
        return (f"""{self.title} ({self.year}) - {self.views_nr} wyświetleń""")

    def play(self):
        return self.views_nr + 1

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
    
    def __str__(self):
        return (f"""{self.title} S{self.season:02}E{self.episode:02} - {self.views_nr} wyświetleń""")

def get_movies(list_of_movies):
    only_movies = list(filter(lambda movie: type(movie) == Movie, list_of_movies))
    return only_movies

def get_series(list_of_series):
    only_series = list(filter(lambda series: type(series) == Series, list_of_series))
    return only_series

def search(list_of_titles, name):
    chosen_title = list(filter(lambda title: title.title == name, list_of_titles))
    if chosen_title:
        return True
    else:
        return False

def generate_views(list_of_titles):
    title = random.choice(list_of_titles)
    title.views_nr = random.choice(range(1,100))
    return

def top_titles(list_of_titles, top_number):
    sorted_list = sorted(list_of_titles, key=lambda title: title.views_nr, reverse=True)[:top_number]
    return sorted_list

def fill_the_database():
    list_of_titles = []
    list_of_titles.append(Series(title="Czterdziestolatek", year="1974", genre="comedy", views_nr = 0, season=1, episode=1))
    list_of_titles.append(Series(title="Czterdziestolatek", year="1974", genre="comedy", views_nr = 0, season=1, episode=2))
    list_of_titles.append(Series(title="Czterdziestolatek", year="1974", genre="comedy", views_nr = 0, season=1, episode=3))
    list_of_titles.append(Series(title="Czterdziestolatek", year="1974", genre="comedy", views_nr = 0, season=1, episode=4))
    list_of_titles.append(Series(title="Czterdziestolatek", year="1974", genre="comedy", views_nr = 0, season=1, episode=5))
    list_of_titles.append(Series(title="Zagubieni", year="2004", genre="drama", views_nr = 0, season=1, episode=1))
    list_of_titles.append(Series(title="Zagubieni", year="2004", genre="drama", views_nr = 0, season=1, episode=2))
    list_of_titles.append(Series(title="Zagubieni", year="2004", genre="drama", views_nr = 0, season=1, episode=3))
    list_of_titles.append(Series(title="Zagubieni", year="2004", genre="drama", views_nr = 0, season=2, episode=1))
    list_of_titles.append(Series(title="Zagubieni", year="2004", genre="drama", views_nr = 0, season=2, episode=2))
    list_of_titles.append(Series(title="Zagubieni", year="2004", genre="drama", views_nr = 0, season=2, episode=3))
    list_of_titles.append(Movie(title="Rocky 2", year="1979", genre="drama", views_nr = 0))
    list_of_titles.append(Movie(title="Rocky 3", year="1982", genre="drama", views_nr = 0))
    list_of_titles.append(Movie(title="Rocky 4", year="1985", genre="drama", views_nr = 0))
    list_of_titles.append(Movie(title="Marsjanin", year="2015", genre="sci-fi", views_nr = 0))
    return list_of_titles

def main():
    cls()
    today = date.today()
    titles = fill_the_database()

    print(f"""
Biblioteka filmów
Najpopularniejsze filmy i seriale dnia {today.strftime("%d.%m.%Y")}""")

    for _ in range (11):
        generate_views(titles)

    top_number = 3 #Liczba określająca ile topowych tytułów będzie wyświetlanych
    top_titles_list = top_titles(titles, top_number)
    for item in range(top_number):
        print (top_titles_list[item])
    
    title_to_be_found = "Zagubienie" #zmienna przechowująca tytuł do odnalezienia. Oczywiście można byłoby ją pobierać od użytkownika
    result = search(titles, title_to_be_found)
    if result:
        print(f"""Ten tytuł znajduje się w bazie""")
    else:
        print(f"""Niestety nie mamy tego tytułu. Sprawdź poprawność wpisanej nazwy""")

main()