from service.inchiriere_service import InchiriereService
from repository.inchiriere_repository import InchiriereFileRepository
from repository.film_repository import FilmFileRepository
from repository.client_repository import ClientFileRepository
from utils.file_utils import copy_file_content, clear_file_content
from domain.validator import  ValidatorInchiriere
from unittest import TestCase

class Teste_service_inchiriere_file(TestCase):

    def setUp(self):
        clear_file_content('../teste_repository/test_inchirieri.txt')
        copy_file_content('../teste_repository/default_inchirieri.txt', '../teste_repository/test_inchirieri.txt')
        repo_inchiriere = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")

        clear_file_content('../teste_repository/test_filme.txt')
        copy_file_content('../teste_repository/default_filme.txt', '../teste_repository/test_filme.txt')
        repo_film = FilmFileRepository("../teste_repository/test_filme.txt")

        clear_file_content('../teste_repository/test_clienti.txt')
        copy_file_content('../teste_repository/default_clienti.txt', '../teste_repository/test_clienti.txt')
        repo_client = ClientFileRepository("../teste_repository/test_clienti.txt")

        validator = ValidatorInchiriere()

        self.inchiriere_service = InchiriereService(repo_inchiriere, validator, repo_film, repo_client)


    def test_add_inchiriere_file(self):
        self.inchiriere_service.add_inchiriere(88, 48, '-')
        list_inchirieri = self.inchiriere_service.get_all_inchirieri()
        assert (len(list_inchirieri) == 8)

    def test_get_clienti_nr_filme_inchiriate_ordonati(self):
        assert (len(self.inchiriere_service.get_clienti_nr_filme_inchiriate_ordonati()) == 5)
        assert (self.inchiriere_service.get_clienti_nr_filme_inchiriate_ordonati()[2].get_id_client() == 65)

    def test_get_clienti_nr_filme_inchiriate_sortnume(self):
        assert (len(self.inchiriere_service.get_clienti_nr_filme_inchiriate_sortnume()) == 5)
        assert (self.inchiriere_service.get_clienti_nr_filme_inchiriate_sortnume()[4].get_nume() == 'Maria')
        assert (self.inchiriere_service.get_clienti_nr_filme_inchiriate_sortnume()[1].get_nume() == 'Cristian')

    def test_get_filme_nr_clienti_ordonate(self):
        assert (len(self.inchiriere_service.get_filme_nr_clienti_ordonate(3)) == 3)
        assert (self.inchiriere_service.get_filme_nr_clienti_ordonate(3)[0].get_id_film() == 13)
        assert (self.inchiriere_service.get_filme_nr_clienti_ordonate(4)[1].get_id_film() == 92)

    def test_get_filme_nr_inchirieri_mic(self):
        assert (len(self.inchiriere_service.get_filme_nr_inchirieri_mic(3)) == 3)
        assert (self.inchiriere_service.get_filme_nr_inchirieri_mic(3)[0].get_id_film() == 88)
        assert (self.inchiriere_service.get_filme_nr_inchirieri_mic(4)[3].get_id_film() == 13)

    def test_get_clienti_nr_filme_inchiriate_procent(self):
        assert (len(self.inchiriere_service.get_clienti_nr_filme_inchiriate_procent(20)) == 1)
        assert (len(self.inchiriere_service.get_clienti_nr_filme_inchiriate_procent(45)) == 2)
        assert (self.inchiriere_service.get_clienti_nr_filme_inchiriate_procent(45)[1].get_id_client() == 38)





