from domain.film import Film
from exception import *

class FilmInMemoryRepository:

    def __init__(self):
        self.__film_stocare = {}

    def add_film(self, film):
        """
        Adauga film
        :param film: obiect;  filmul de adaugat
        :return: - ;dictioanrul de filme se modifica prin adaugarea la sfarsit a filmului
        :raises: ValueError daca exista deja film cu id-ul dat
        """
        id_film = film.get_id_film()
        if id_film in self.__film_stocare:
            raise Exception("id film existent")
        self.__film_stocare[id_film] = film

    def delete_film(self, id_film_delete):
        """
        Sterge film
        :param id_film_delete: int
        :return: -
        """
        if id_film_delete not in self.__film_stocare:
            raise NuExistaAcestIdFilmException()
        self.__film_stocare.pop(id_film_delete)

    def find_film(self, id_film_find):
        """
        Cauta film dupa id
        :param id_film_find: int
        :return: obiectul cu id ul introdus sau exceptie
        """
        if id_film_find not in self.__film_stocare:
            raise Exception("Nu exista un film cu acest id")
        return self.__film_stocare[id_film_find]

    def update_film(self, id_film_update, film):
        """
        Modifica(update) filmul cu id ul dat
        :param id_film_update: int
        :param film; obiect
        :return: - sau exception
        """
        if id_film_update not in self.__film_stocare:
            raise Exception("Nu exista film cu id-ul introdus")
        self.__film_stocare[id_film_update] = film


    def get_all(self):
        """
        Returneaza toate filmele
        :return: dictionar
        """
        return [self.__film_stocare[i] for i in self.__film_stocare.keys()]

    def size_filme(self):
        return len(self.get_all())






class FilmFileRepository(FilmInMemoryRepository):

    def __init__(self, filename):
        FilmInMemoryRepository.__init__(self)
        self.__filename = filename
        self.load_from_file()

    def load_from_file(self):
        """
        Incarca datele despre film din fisier
        """
        with open(self.__filename, mode='r', encoding='utf-8') as filme_file:
            lines = filme_file.readlines()
            lines = [line.strip() for line in lines if line.strip() != '']
            for line in lines:
                id_film, titlu, descriere, gen = line.split(',')
                id_film = id_film.strip()
                titlu= titlu.strip()
                descriere = descriere.strip()
                gen = gen.strip()
                FilmInMemoryRepository.add_film(self, Film(int(id_film), titlu, descriere, gen))

    def add_film(self, film: Film):
        """
        Adauga film dat
        :param film: filmul care se adauga
        :type film: Film
        :return: -; fisierul in care se tin filmele se modifica,
                    lista curenta de filme se modifica prin adugare
        :raises: ValueError daca exista deja filme cu id dat
        """
        FilmInMemoryRepository.add_film(self, film)
        self.write_to_file()


    def write_to_file(self):
        """
        Scrie datele filmelor in fisier
        """
        filme = FilmInMemoryRepository.get_all(self)
        filme = [str(film.get_id_film()) + ',' + film.get_titlu() + ',' + film.get_descriere() + ',' + film.get_gen()  for film in filme]
        with open(self.__filename, mode='w', encoding='utf-8') as filme_file:
            text_to_write = '\n'.join(filme)
            filme_file.write(text_to_write)

    def delete_film(self, id_film_delete):
        """
        Sterge film cu id dat
        :param id_film_delete: int
        :return: filmul cu id dat este sters din fisier, din lista curenta
        :rtype: -;
        :raises: ValueError daca nu exista film cu id_film dat
        """
        deleted_film = FilmInMemoryRepository.delete_film(self, id_film_delete)
        self.write_to_file()
        return deleted_film

    def update_film(self, id_film_update, film):
        """
        Modifica filmul cu id dat
        :param id_film_update: int
        :param film: Film
        :return: -; filmul cu id-ul dat se modifica, daca exista, atat in fisier cat si in lista curenta
        :rtype: -;
        :raises: ValueError daca nu exista film cu id_ul dat
        """
        FilmInMemoryRepository.update_film(self, id_film_update, film)
        self.write_to_file()

    def find_film(self, id_film_find):
        """
        Cauta film dupa id
        :param id_film: int
        :return: obiectul cu id ul introdus sau exceptia
        """
        return FilmInMemoryRepository.find_film(self, id_film_find)

    def get_all(self):

        return FilmInMemoryRepository.get_all(self)

    def size_filme(self):
        return FilmInMemoryRepository.size_filme(self)


