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
            f" Tytuł: {self.name}\n rok prod.: {self.year}\n gatunek: {self._type}\n "
            f" liczba odtworzeń: {self.num_plays}"
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
            f" Tytuł: {self.name}\n rok prod.: {self.year}\n gatunek: {self._type}\n  "
            f"ilość odcinków: {self.episodes}\n ilość sezonów:{self.seasons}\n ilość odtworzeń: {self.num_plays}"
        )


_list = []
pulp_fiction = Movies("Pulp fiction", 1994, "crime", 0)
killing_zoe = Movies("Killing Zoe", 1994, "crime", 0)
amelie = Movies("Amelie", 2001, "romantic-comedy", 0)
trainspotting = Movies("Trainspotting", 1995, "drama", 0)
Pi = Movies("Pi", 1996, "drama", 0)
delicatessen = Movies("Delicatessen", 1992, "comedy/thriller", 0)
breaking_bad = Series(3, 45, "breaking bad", 2012, "crime", 0)
queens_gambit = Series(1, 7, "Queen's gambit", 2020, "moral/comedy", 0)
mr_bean = Series(1, 110, "Mr Bean", 1994, "comedy", 0)
_list.append(pulp_fiction)
_list.append(killing_zoe)
_list.append(amelie)
_list.append(trainspotting)
_list.append(Pi)
_list.append(delicatessen)
_list.append(breaking_bad)
_list.append(queens_gambit)
_list.append(mr_bean)

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
    info = "Nie posiadamy takiego filmu w zasobach"
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
# print(_list)

today = date.today()
today_date = today.strftime("%d.%m.%Y")
name_movie = input("Podaj film który Ciebie interesuje: ")
print(search(name_movie))
result = top_titles()
top3 = result[0:3]
print(f"Dzisiaj: {today_date} najpopularniejsze 3 filmy to: {top3}")
