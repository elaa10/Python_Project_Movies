from domain.inchirieri import Inchiriere
from domain.validator import *
from domain.film import Film
from domain.client import Client

class Teste_inchiriere_domain:

    def test_create_inchiriere(self):
        film = Film(3, "Atonment", "f_bun", "razboi")
        client = Client(3, "Alexandra",637562742734)
        status_returnare = '-'
        inchiriere = Inchiriere(film, client, status_returnare)
        assert inchiriere.get_film() == film
        assert inchiriere.get_client() == client
        assert 1 != 1
