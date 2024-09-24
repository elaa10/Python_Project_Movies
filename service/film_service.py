from domain.film import Film
from domain.validator import ValidatorFilm
import random

class FilmService:

    def __init__(self, FilmInMemoryRepository, ValidatorFilm):
        self.__repo_film = FilmInMemoryRepository
        self.__validator_film = ValidatorFilm

    def add_film(self, id_film, titlu, descriere, gen):
        """
        Creaza obiectul film, il valideaza si apeleaza add film din repo
        :param id_film: int
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return: -
        :raises: ValueError daca filmul de adaugat nu este valid, daca filmul exista deja
        """
        film = Film(id_film, titlu, descriere, gen)
        self.__validator_film.valideaza_film(film)
        self.__repo_film.add_film(film)

    def delete_film(self, id_film_delete):
        """
        Apeleaza delete film din repo
        :param id_film_delete: int
        :return: -
        :raises: ValueError daca nu exista film cu id dat
        """
        self.__repo_film.delete_film(id_film_delete)

    def find_film(self, id_film_find):
        """
        Apeleaza find film din repo
        :param id_film_find: int
        :return: returneaza filmul cautat sau raise exception daca mnu exista film cu acel id
        """
        return self.__repo_film.find_film(id_film_find)

    def update_film(self, id_film_update, titlu_nou, descriere_nou, gen_nou):
        """
        Creaza noul obiect Film, il valideaza si apeleaza update film din repo
        :param id_film_update: int
        :param titlu_nou: string
        :param descriere_nou: string
        :param gen_nou: string
        :return: -
        """
        film = Film(id_film_update, titlu_nou, descriere_nou, gen_nou)
        self.__validator_film.valideaza_film(film)
        self.__repo_film.update_film(id_film_update, film)

    def genereaza_filme(self, nr_generare):
        """
        Genereaza atributele filmului si apeleaza add_film
        :param nr_generare: int
        :return: -
        """
        sir_titluri = ['Atonement', 'Libertate', 'Shutter_Island', 'The_Great_Gatsby', 'Oppenheimer', 'Gia', 'Inception', 'Wind_River']
        sir_descrieri = ['foarte_bun', 'aesthetic', 'filozofic', 'abstract', 'bonding', 'genial', 'emotionand', 'revelator', 'inspirational']
        sir_gen = ['drama', 'razboi', 'actiune', 'aventura', 'istoric', 'mister', 'thriller']
        if nr_generare == 0:
            return
        else:
            id_film = random.randint(0, 100)
            titlu = random.choice(sir_titluri)
            descriere = random.choice(sir_descrieri)
            gen = random.choice(sir_gen)
            try:
                self.add_film(id_film, titlu, descriere, gen)
            except Exception:
                return self.genereaza_filme(nr_generare)
            nr_generare -= 1
            return self.genereaza_filme(nr_generare)

    def get_all_filme(self):
        """
        Returneaza dictionarul toate filmele
        """
        return self.__repo_film.get_all()

    def size_filme(self):
        return len(self.get_all_filme())
