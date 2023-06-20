from random import randint, choice
from datetime import date


class Movies:
    def __init__(self, name, year, _type, num_plays):
        self.name = name
        self.year = year
        self._type = _type
        self.num_plays = num_plays

    def __str__(self):
        return (
            f" Tytuł: {self.name}\n Rok produkcji: {self.year}\n Gatunek: {self._type}\n "
            f" Liczba odtworzeń: {self.num_plays}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def play(self, num_plays):
        self.num_plays += 1


class Series(Movies):
    def __init__(self, episodes, seasons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episodes = episodes
        self.seasons = seasons

    def __str__(self):
        return (
            f" Tytuł: {self.name}\n Rok produkcji: {self.year}\n Gatunek: {self._type}\n  "
            f"Ilość odcinków: {self.episodes}\n Ilość sezonów:{self.seasons}\n Liczba odtworzeń: {self.num_plays}"
        )


_list = []
zielona_mila = Movies("Zielona Mila", 1999, "dramat", 0)
skazani_na_Shawshank = Movies("Skazani na Shawshank", 1994, "dramat", 0)
forest_gump = Movies("Forest Gump", 1994, "dramat", 0)
leon_zawodowiec = Movies("Leon zawodowiec", 1994, "kryminał", 0)
requiem_dla_snu = Movies("Requiem dla snu", 200, "dramat", 0)
matrix = Movies("Matrix", 1999, "sci-fi", 0)
milczenie_owiec = Movies("Milczenie owiec", 1991, "thriller", 0)
gladiator = Movies("Gladiator", 2000, "dramat historyczny", 0)
avatar = Movies("Avatar", 2009, "sci-fi", 0)
shrek = Movies("Shrek", 2001, "familijny", 0)
gra_o_tron = Series(10, 8, "Gra o tron", 2011 - 2019, "przygodowy", 0)
dr_house = Series(22, 8, "Dr House", 2004 - 2012, "komedia", 0)
breaking_bad = Series(7, 5, "Breaking Bad", 2008 - 2013, "kryminał", 0)
stranger_things = Series(8, 5, "Stranger Things", 2016, "sci-fi", 0)
przyjaciele = Series(24, 10, "Przyjaciele", 1994 - 2004, "komedia", 0)
sherlock = Series(3, 4, "Sherlock", 2010 - 2017, "kryminał", 0)
house_of_cards = Series(8, 6, "House of Cards", 2013 - 2018, "Dramat", 0)
dexter = Series(12, 8, "Dexter", 2006 - 2013, "kryminał", 0)
detektyw = Series(8, 4, "Detektyw", 2014, "kryminał", 0)
the_walking_dead = Series(24, 11, "The Walking Dead", 2010 - 2022, "horror", 0)
_list.append(zielona_mila)
_list.append(skazani_na_Shawshank)
_list.append(forest_gump)
_list.append(leon_zawodowiec)
_list.append(requiem_dla_snu)
_list.append(matrix)
_list.append(milczenie_owiec)
_list.append(gladiator)
_list.append(avatar)
_list.append(shrek)
_list.append(gra_o_tron)
_list.append(dr_house)
_list.append(breaking_bad)
_list.append(stranger_things)
_list.append(przyjaciele)
_list.append(sherlock)
_list.append(house_of_cards)
_list.append(dexter)
_list.append(detektyw)
_list.append(the_walking_dead)

movies_list = []
series_list = []
top_list = []


def get_movies():
    for movie in _list:
        if isinstance(movie, Movies) == True:
            movies_list.append(movie)


def get_series():
    for serie in _list:
        if isinstance(movie, Series) == True:
            series_list.append(serie)


def search(name_movie):
    for movie in _list:
        if movie.name == name_movie:
            return movie
    for serie in series_list:
        if serie.name == name_movie:
            return serie
    info = "Nie ma takiego filmu w bazie"
    return info


def generate_views(plays):
    for x in range(plays):
        movie_random = choice(_list)
        movie_random.num_plays = randint(0, 100)


def top_titles():
    top_titles_list = []
    top_movies = sorted(_list, key=lambda movie: movie.num_plays, reverse=True)
    for movie in top_movies:
        title = movie.name
        top_titles_list.append(title)
    return top_titles_list


generate_views(10)
print(_list)

today = date.today()
today_date = today.strftime("%d.%m.%Y")
name_movie = input("Podaj tytuł filmu: ")
print(search(name_movie))
result = top_titles()
top3 = result[0:3]
print(f"Dzisiaj: {today_date} najpopularniejsze 3 filmy to: {top3}")
