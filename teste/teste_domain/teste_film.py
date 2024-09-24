from domain.film import Film
from domain.validator import *
from unittest import TestCase

class Teste_film_domain(TestCase):

    def test_create_film(self):
        id_film = 1
        titlu = "Atonment"
        descriere = "f_bun"
        gen = "razboi"
        film = Film(id_film, titlu, descriere, gen)
        assert film.get_id_film() == id_film
        assert film.get_titlu() == titlu
        assert film.get_descriere() == descriere
        assert film.get_gen() == gen

    def test_validate_film(self):
        film = Film(-3, "Atonment", "f_bun", "razboi")
        validator = ValidatorFilm()
        try:
            validator.valideaza_film(film)
            assert False
        except Exception:
            assert True

    def run_all_tests(self):
        self.__test_create_film()
        self.__test_validate_film()