from service.client_service import ClientService
from domain.validator import ValidatorClient
from repository.client_repository import ClientInMemoryRepository, ClientFileRepository
from utils.file_utils import copy_file_content, clear_file_content

class Teste_service_client:

    def test_add_client(self):
        repo = ClientInMemoryRepository()
        validator = ValidatorClient()
        client_service = ClientService(repo, validator)
        client_service.add_client(3, "Alexandra", str(6375627427342))
        test_clienti_list = client_service.get_all_clienti()
        assert (len(test_clienti_list) == 1)

        try:
            client_service.add_client(3, "Alexandra", str(637562742734))
            assert False
        except:
            assert True

    def test_update_client(self):
        repo = ClientInMemoryRepository()
        validator = ValidatorClient()
        client_service = ClientService(repo, validator)
        client_service.add_client(3, "Alexandra", str(6375622742734))
        client_service.add_client(2, "Ioana", str(6375627242734))
        client_service.update_client(3, "Maria", str(6375622742734))
        assert (repo.find_client(3).get_nume() == 'Maria')

    def test_add_client_file(self):

        clear_file_content('../teste_repository/test_clienti.txt')
        repo = ClientFileRepository("../teste_repository/test_clienti.txt")
        validator = ValidatorClient()
        client_service = ClientService(repo, validator)
        client_service.add_client(3, "Alexandra", str(6375627427342))
        test_clienti_list = client_service.get_all_clienti()
        assert (len(test_clienti_list) == 1)

        try:
            client_service.add_client(3, "Alexandra", str(637562742734))
            assert False
        except:
            assert True

    def test_update_client_file(self):
        clear_file_content('../teste_repository/test_clienti.txt')
        repo = ClientFileRepository("../teste_repository/test_clienti.txt")
        validator = ValidatorClient()
        client_service = ClientService(repo, validator)
        client_service.add_client(3, "Alexandra", str(6375262742734))
        client_service.add_client(2, "Ioana", str(6375627242734))
        client_service.update_client(3, "Maria", str(6375622742734))
        assert (repo.find_client(3).get_nume() == 'Maria')

