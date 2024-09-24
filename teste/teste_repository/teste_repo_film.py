from domain.film import Film
from repository.film_repository import FilmInMemoryRepository, FilmFileRepository
from utils.file_utils import copy_file_content, clear_file_content
from unittest import TestCase
from exception import *

class Teste_repo_film:

    def test_adauga_film(self):

        film1 = Film(1, "Atonment","f_bun","razboi")
        film2 = Film(2, "Atonment","f_bun","razboi")

        repo_film = FilmInMemoryRepository()
        repo_film.add_film(film1)
        repo_film.add_film(film2)
        assert (len(repo_film.get_all()) == 2)

    def test_delete_film(self):
        film1 = Film(1, "Atonment","f_bun","razboi")
        film2 = Film(2, "Atonment", "f_bun", "razboi")

        repo_film = FilmInMemoryRepository()
        repo_film.add_film(film1)
        repo_film.add_film(film2)

        id_film_delete = 3
        try:
            repo_film.delete_film(id_film_delete)
            assert False
        except Exception :
            assert True
        id_film_delete = 1
        repo_film.delete_film(id_film_delete)
        assert (len(repo_film.get_all()) == 1)

    def test_find_film(self):
        film1 = Film(1, "Atonment","superb","razboi")
        film2 = Film(2, "Atonment", "f_bun", "razboi")
        film3 = Film(3, "Atonment", "f_bun", "razboi")

        repo_film = FilmInMemoryRepository()
        repo_film.add_film(film1)
        repo_film.add_film(film2)
        repo_film.add_film(film3)
        id_film_find = 4
        try:
            repo_film.find_film(id_film_find)
            assert False
        except Exception :
            assert True
        id_film_find = 1
        assert (repo_film.find_film(id_film_find).get_id_film() == 1)
        assert (repo_film.find_film(id_film_find).get_descriere() == "superb")

    def test_update_film(self):
        film1 = Film(1, "Atonment","superb","razboi")
        film2 = Film(2, "Atonment", "f_bun", "razboi")
        film3 = Film(3, "Atonment", "f_bun", "razboi")

        repo_film = FilmInMemoryRepository()
        repo_film.add_film(film1)
        repo_film.add_film(film2)
        repo_film.add_film(film3)
        id_film_update = 4
        film_update = Film(4, 'Parasite', 'korean', 'drama')
        try:
            repo_film.update_film(id_film_update, film_update)
            assert False
        except Exception :
            assert True
        id_film_update = 2
        film_update = Film(2, 'Parasite', 'korean', 'drama')
        repo_film.update_film(id_film_update, film_update)
        assert (repo_film.find_film(id_film_update).get_titlu() == 'Parasite')



class Teste_repo_film_file(TestCase):

    def setUp(self):
        #cod executat inainte de fiecare metoda din aceasta clasa
        clear_file_content('../teste_repository/test_filme.txt')
        self.test_repo = FilmFileRepository("../teste_repository/test_filme.txt")

    def tearDown(self):
        # cod executat dupa fiecare metoda din aceasta clasa
        clear_file_content('../teste_repository/test_filme.txt')

    def test_read_from_file(self):
        copy_file_content('../teste_repository/default_filme.txt', '../teste_repository/test_filme.txt')
        self.test_repo = FilmFileRepository("../teste_repository/test_filme.txt")
        self.assertEqual(self.test_repo.size_filme(), 6)


    def test_adauga_film_file(self):

        film1 = Film(1, "Atonment","f_bun","razboi")
        film2 = Film(2, "Atonment","f_bun","razboi")

        self.test_repo.add_film(film1)
        self.test_repo.add_film(film2)
        self.assertEqual(len(self.test_repo.get_all()), 2)

    def test_delete_film_file(self):

        film1 = Film(1, "Atonment","f_bun","razboi")
        film2 = Film(2, "Atonment", "f_bun", "razboi")

        self.test_repo.add_film(film1)
        self.test_repo.add_film(film2)

        id_film_delete = 3
        self.assertRaises(NuExistaAcestIdFilmException, self.test_repo.delete_film, id_film_delete)
        # try:
        #     repo_film.delete_film(id_film_delete)
        #     assert False
        # except Exception :
        #     assert True
        id_film_delete = 1
        self.test_repo.delete_film(id_film_delete)
        self.assertEqual(len(self.test_repo.get_all()), 1)

    def test_find_film_file(self):

        film1 = Film(1, "Atonment","superb","razboi")
        film2 = Film(2, "Atonment", "f_bun", "razboi")
        film3 = Film(3, "Atonment", "f_bun", "razboi")
        self.test_repo.add_film(film1)
        self.test_repo.add_film(film2)
        self.test_repo.add_film(film3)
        id_film_find = 4
        try:
            self.test_repo.find_film(id_film_find)
            assert False
        except Exception :
            assert True
        id_film_find = 1
        self.assertEqual(self.test_repo.find_film(id_film_find).get_id_film(), 1)
        self.assertEqual(self.test_repo.find_film(id_film_find).get_descriere(), "superb")



    def test_update_film_file(self):

        film1 = Film(1, "Atonment","superb","razboi")
        film2 = Film(2, "Atonment", "f_bun", "razboi")
        film3 = Film(3, "Atonment", "f_bun", "razboi")

        self.test_repo.add_film(film1)
        self.test_repo.add_film(film2)
        self.test_repo.add_film(film3)
        id_film_update = 4
        film_update = Film(4, 'Parasite', 'korean', 'drama')
        try:
            self.test_repo.update_film(id_film_update, film_update)
            assert False
        except Exception :
            assert True
        id_film_update = 2
        film_update = Film(2, 'Parasite', 'korean', 'drama')
        self.test_repo.update_film(id_film_update, film_update)
        self.assertEqual(self.test_repo.find_film(id_film_update).get_titlu(), 'Parasite')





