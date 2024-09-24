from domain.client import Client
from domain.validator import ValidatorClient
from repository.client_repository import ClientInMemoryRepository
import random


class ClientService:

    def __init__(self, ClientInMemoryRepository, ValidatorClient):
        self.__repo_client = ClientInMemoryRepository
        self.__validator_client = ValidatorClient

    def add_client(self, id_client, nume, cnp):
        """
        Creaza obiectul client, il valideaza si apeleaza add client din repo
        :param id_client: int
        :param nume: string
        :param cnp: string
        :return:
        :raises: ValueError daca clientul de adaugat nu este valid, daca clientul exista deja
        """
        client = Client(id_client, nume, cnp)
        self.__validator_client.valideaza_client(client)
        self.__repo_client.add_client(client)

    def delete_client(self, id_client_delete):
        """
        Apeleaza delete client din repo
        :param id_client_delete: int
        :return: -
        """
        self.__repo_client.delete_client(id_client_delete)

    def find_client(self, id_client_find):
        """
        Apeleaza find client din repo
        :param id_client_find: int
        :return: clientul cu id ul introdus sau raise exception
        """
        return self.__repo_client.find_client(id_client_find)

    def update_client(self, id_client_update, nume_nou, cnp_nou):
        """
                Creaza noul obiect Client, il valideaza si apeleaza update client din repo
                :param id_client_update: int
                :param  nume_nou: string
                :param cnp_nou: string
                :return: -
        """
        client = Client(id_client_update, nume_nou, cnp_nou)
        self.__validator_client.valideaza_client(client)
        self.__repo_client.update_client(id_client_update, client)

    def genereaza_clienti(self, nr_generare):
        """
        Genereaza atributele clientului si apeleaza add_client
        :param nr_generare: int
        :return: -
        """
        sir_nume = ['Alexandra', 'Ioana', 'Maria', 'Vlad', 'Cristian', 'Tudor']
        sir_cnp = ['1901102410929', '1901102295126', '1901102298201', '5040910272565', '5040910277820']
        if nr_generare == 0:
            return
        else:
            id_client = random.randint(0, 100)
            nume = random.choice(sir_nume)
            cnp = random.choice(sir_cnp)
            try:
                self.add_client(id_client, nume, cnp)
            except Exception:
                return self.genereaza_clienti(nr_generare)
            nr_generare -= 1
            return self.genereaza_clienti(nr_generare)


    def get_all_clienti(self):
        """
               Returneaza dictionarul cu toti clientii
        """
        return self.__repo_client.get_all()