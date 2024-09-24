from domain.client import Client
from repository.client_repository import ClientInMemoryRepository, ClientFileRepository
from utils.file_utils import copy_file_content, clear_file_content

class Teste_repo_client:

    def test_adauga_client(self):
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Alexandra",637562742734)

        repo_client = ClientInMemoryRepository()
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        assert(len(repo_client.get_all()) == 2)

    def test_delete_client(self):
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Alexandra", 637562742734)

        repo_client = ClientInMemoryRepository()
        repo_client.add_client(client1)
        repo_client.add_client(client2)

        id_client_delete = 1
        try:
            repo_client.delete_client(id_client_delete)
            assert False
        except Exception :
            assert True
        id_client_delete = 2
        repo_client.delete_client(id_client_delete)
        assert (len(repo_client.get_all()) == 1)

    def test_find_client(self):
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Ioana", 637562742734)

        repo_client = ClientInMemoryRepository()
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        id_client_find = 4
        try:
            repo_client.find_client(id_client_find)
            assert False
        except Exception :
            assert True
        id_client_find = 2
        assert (repo_client.find_client(id_client_find).get_id_client() == 2)
        assert (repo_client.find_client(id_client_find).get_nume() == "Ioana")


    def test_update_client(self):
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Ioana", 637562742734)

        repo_client = ClientInMemoryRepository()
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        id_client_update = 4
        client_update = Client(4, 'Maria', 1234567890123)
        try:
            repo_client.update_client(id_client_update, client_update)
            assert False
        except Exception :
            assert True
        id_client_update = 2
        client_update = Client(2, 'Maria', 1234567890123)
        repo_client.update_client(id_client_update, client_update)
        assert (repo_client.find_client(id_client_update).get_nume() == 'Maria')

    def test_read_from_file(self):
        clear_file_content('../teste_repository/test_clienti.txt')
        copy_file_content('../teste_repository/default_clienti.txt', '../teste_repository/test_clienti.txt')
        test_repo = ClientFileRepository("../teste_repository/test_clienti.txt")
        assert (test_repo.size_clienti() == 8)

    def test_adauga_client_file(self):

        clear_file_content('../teste_repository/test_clienti.txt')
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Alexandra",637562742734)

        repo_client = ClientFileRepository("../teste_repository/test_clienti.txt")
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        assert(len(repo_client.get_all()) == 2)

    def test_delete_client_file(self):

        clear_file_content('../teste_repository/test_clienti.txt')
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Alexandra", 637562742734)

        repo_client = ClientFileRepository("../teste_repository/test_clienti.txt")
        repo_client.add_client(client1)
        repo_client.add_client(client2)

        id_client_delete = 1
        try:
            repo_client.delete_client(id_client_delete)
            assert False
        except Exception :
            assert True
        id_client_delete = 2
        repo_client.delete_client(id_client_delete)
        assert (len(repo_client.get_all()) == 1)

    def test_find_client_file(self):

        clear_file_content('../teste_repository/test_clienti.txt')
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Ioana", 637562742734)

        repo_client = ClientFileRepository("../teste_repository/test_clienti.txt")
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        id_client_find = 4
        try:
            repo_client.find_client(id_client_find)
            assert False
        except Exception :
            assert True
        id_client_find = 2
        assert (repo_client.find_client(id_client_find).get_id_client() == 2)
        assert (repo_client.find_client(id_client_find).get_nume() == "Ioana")


    def test_update_client_file(self):

        clear_file_content('../teste_repository/test_clienti.txt')
        client1 = Client(3, "Alexandra", 637562742734)
        client2 = Client(2, "Ioana", 637562742734)

        repo_client = ClientFileRepository("../teste_repository/test_clienti.txt")
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        id_client_update = 4
        client_update = Client(4, 'Maria', 1234567890123)
        try:
            repo_client.update_client(id_client_update, client_update)
            assert False
        except Exception :
            assert True
        id_client_update = 2
        client_update = Client(2, 'Maria', 1234567890123)
        repo_client.update_client(id_client_update, client_update)
        assert (repo_client.find_client(id_client_update).get_nume() == 'Maria')

