from service.film_service import FilmService
from domain.validator import ValidatorFilm
from repository.film_repository import FilmInMemoryRepository, FilmFileRepository
from utils.file_utils import copy_file_content, clear_file_content

class Teste_service_film:

    def test_add_film(self):
        repo = FilmInMemoryRepository()
        validator = ValidatorFilm()
        film_service = FilmService(repo, validator)
        film_service.add_film(1, "Atonment","f_bun","razboi")
        test_filme_list = film_service.get_all_filme()
        assert (len(test_filme_list) == 1)

        try:
            film_service.add_film(1, "Adt", "f_bun", "razboi")
            assert False
        except:
            assert True

    def test_delete(self):
        repo = FilmInMemoryRepository()
        validator = ValidatorFilm()
        film_service = FilmService(repo, validator)
        film_service.add_film(1, "Atonment","f_bun","razboi")
        film_service.add_film(2, "Atonment", "f_bun", "razboi")
        film_service.add_film(3, "Atonment", "f_bun", "razboi")
        film_service.delete_film(3)
        test_filme_list = film_service.get_all_filme()
        assert (len(test_filme_list) == 2)

    def test_update(self):
        repo = FilmInMemoryRepository()
        validator = ValidatorFilm()
        film_service = FilmService(repo, validator)
        film_service.add_film(1, "Atonment","f_bun","razboi")
        film_service.add_film(2, "Atonment", "f_bun", "razboi")
        film_service.add_film(3, "Atonment", "f_bun", "razboi")
        film_service.update_film(3, "inception", "f_bun", "razboi")
        assert (repo.find_film(3).get_titlu() == 'inception')

    def test_add_film_file(self):

        clear_file_content('../teste_repository/test_filme.txt')
        repo = FilmFileRepository('../teste_repository/test_filme.txt')
        validator = ValidatorFilm()
        film_service = FilmService(repo, validator)
        film_service.add_film(1, "Atonment","f_bun","razboi")
        test_filme_list = film_service.get_all_filme()
        assert (len(test_filme_list) == 1)

        try:
            film_service.add_film(1, "Adt", "f_bun", "razboi")
            assert False
        except:
            assert True

    def test_delete_file(self):
        clear_file_content('../teste_repository/test_filme.txt')
        repo = FilmFileRepository('../teste_repository/test_filme.txt')
        validator = ValidatorFilm()
        film_service = FilmService(repo, validator)
        film_service.add_film(1, "Atonment","f_bun","razboi")
        film_service.add_film(2, "Atonment", "f_bun", "razboi")
        film_service.add_film(3, "Atonment", "f_bun", "razboi")
        film_service.delete_film(3)
        test_filme_list = film_service.get_all_filme()
        assert (len(test_filme_list) == 2)

    def test_update_file(self):
        clear_file_content('../teste_repository/test_filme.txt')
        repo = FilmFileRepository('../teste_repository/test_filme.txt')
        validator = ValidatorFilm()
        film_service = FilmService(repo, validator)
        film_service.add_film(1, "Atonment","f_bun","razboi")
        film_service.add_film(2, "Atonment", "f_bun", "razboi")
        film_service.add_film(3, "Atonment", "f_bun", "razboi")
        film_service.update_film(3, "inception", "f_bun", "razboi")
        assert (repo.find_film(3).get_titlu() == 'inception')


