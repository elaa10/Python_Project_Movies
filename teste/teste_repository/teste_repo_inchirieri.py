from repository.inchiriere_repository import InchiriereFileRepository
from utils.file_utils import copy_file_content, clear_file_content
from domain.inchirieri import Inchiriere


class Teste_repo_inchirieri_file():
    def test_read_from_file(self):
        clear_file_content('../teste_repository/test_inchirieri.txt')
        copy_file_content('../teste_repository/default_inchirieri.txt', '../teste_repository/test_inchirieri.txt')
        test_repo = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")
        assert (test_repo.size_inchirieri() == 7)

    def test_adauga_inchiriere_file(self):

        clear_file_content('../teste_repository/test_inchirieri.txt')
        inchiriere1 = Inchiriere(3, 45, '-')
        inchiriere2 = Inchiriere(33, 45,'-')

        test_repo = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")
        test_repo.add_inchiriere(inchiriere1)
        test_repo.add_inchiriere(inchiriere2)
        assert (len(test_repo.get_all()) == 2)

    def test_find_inchiriere_file(self):

        clear_file_content('../teste_repository/test_inchirieri.txt')
        inchiriere1 = Inchiriere(3, 45, '-')
        inchiriere2 = Inchiriere(33, 45, '-')

        test_repo = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")
        test_repo.add_inchiriere(inchiriere1)
        test_repo.add_inchiriere(inchiriere2)
        inchiriere = Inchiriere(3, 45, '-')
        try:
            test_repo.find_inchiriere(inchiriere)
            assert False
        except Exception :
            assert True
        inchiriere = Inchiriere(33, 45, '-')
        assert (test_repo.find_inchiriere(inchiriere) is not None)

    def test_get_clienti_nr_filme(self):
        clear_file_content('../teste_repository/test_inchirieri.txt')
        copy_file_content('../teste_repository/default_inchirieri.txt', '../teste_repository/test_inchirieri.txt')
        test_repo = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")
        assert (len(test_repo.get_clienti_nr_filme()) == 5)


    def test_get_filme_nr_clienti(self):
        clear_file_content('../teste_repository/test_inchirieri.txt')
        copy_file_content('../teste_repository/default_inchirieri.txt', '../teste_repository/test_inchirieri.txt')
        test_repo = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")
        assert (len(test_repo.get_filme_nr_clienti()) == 5)


    def test_get_clienti_nr_filme_simplu(self):
        clear_file_content('../teste_repository/test_inchirieri.txt')
        copy_file_content('../teste_repository/default_inchirieri.txt', '../teste_repository/test_inchirieri.txt')
        test_repo = InchiriereFileRepository("../teste_repository/test_inchirieri.txt")
        assert (len(test_repo.get_clienti_nr_filme_simplu()) == 5)

