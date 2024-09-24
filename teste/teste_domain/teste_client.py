from domain.client import Client
from domain.validator import *
from unittest import TestCase

class Teste_client_domain(TestCase):

    def test_create_client(self):
        id_client = -3
        nume = "Alexandra"
        cnp = 637562742734
        client = Client(id_client, nume, cnp)
        assert client.get_id_client() == id_client
        assert client.get_nume() == nume
        assert client.get_cnp() == cnp


    def test_validate_client(self):
        client = Client(-3, "Alexandra",637562742734)
        validator = ValidatorClient()
        try:
            validator.valideaza_client(client)
            assert False
        except Exception :
            assert True

    # def run_all_tests(self):
    #     self.__test_create_client()
    #     self.__test_validate_client()
