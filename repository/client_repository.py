from domain.client import Client


class ClientInMemoryRepository:

    def __init__(self):
        self.__client_stocare = {}

    def add_client(self, client):
        """
        Adauga client
        :param client: obiect
        :return: -
        """
        id_client = client.get_id_client()
        if id_client in self.__client_stocare:
            raise Exception("id client existent")
        self.__client_stocare[id_client] = client

    def delete_client(self, id_client_delete):
        """
        Sterge client
        :param id_client_delete: int
        :return: -
        """
        if id_client_delete not in self.__client_stocare:
            raise Exception("id client inexistent")
        self.__client_stocare.pop(id_client_delete)

    def find_client(self, id_client_find):
        """
        Cauta client dupa id
        :param id_client_find: int
        :return: clientul cu id ul introdus sau exceptie
        """
        if id_client_find not in self.__client_stocare:
            raise Exception("Nu exista un client cu acest id")
        return self.__client_stocare[id_client_find]

    def update_client(self, id_client_update, client):
        """
        Modifica(update) clientul cu id ul dat
        :param id_client_update: int
        :param cleint: obiect
        :return: - sau exception
        """
        if id_client_update not in self.__client_stocare:
            raise Exception("Nu exista client cu id-ul introdus")
        self.__client_stocare[id_client_update] = client

    def get_all(self):
        """
        Returneaza toti clientii
        :return: dictionar
        """
        return [self.__client_stocare[i] for i in self.__client_stocare.keys()]

    def size_clienti(self):
        return len(self.get_all())


class ClientFileRepository(ClientInMemoryRepository):

    def __init__(self, filename):
        ClientInMemoryRepository.__init__(self)
        self.__filename = filename
        self.load_from_file()

    def load_from_file(self):
        """
        Incarca datele despre client din fisier
        """
        with open(self.__filename, mode='r', encoding='utf-8') as clienti_file:
            lines = clienti_file.readlines()
            lines = [line.strip() for line in lines if line.strip() != '']
            for line in lines:
                id_client, nume, cnp = line.split(',')
                id_client = id_client.strip()
                nume = nume.strip()
                cnp = cnp.strip()
                ClientInMemoryRepository.add_client(self, Client(int(id_client), nume, cnp))

    def add_client(self, client: Client):
        """
        Adauga client dat
        :param client: clientul care se adauga
        :type client: Client
        :return: -; fisierul in care se tin clientii se modifica,
                    lista curenta de clienti se modifica prin adugare
        :raises: ValueError daca exista deja clienti cu id_dat
        """
        ClientInMemoryRepository.add_client(self, client)
        self.write_to_file()


    def write_to_file(self):
        """
        Scrie datele filmelor in fisier
        """
        clienti = ClientInMemoryRepository.get_all(self)
        clienti = [str(client.get_id_client()) + ',' + client.get_nume() + ',' + str(client.get_cnp())   for client in clienti]
        with open(self.__filename, mode='w', encoding='utf-8') as clienti_file:
            text_to_write = '\n'.join(clienti)
            clienti_file.write(text_to_write)

    def delete_client(self, id_client_delete):
        """
        Sterge client cu id dat
        :param id_client_delete: int
        :return: clientul cu id dat este sters din fisier, din lista curenta
        :rtype: -;
        :raises: ValueError daca nu exista client cu id_client dat
        """
        deleted_client = ClientInMemoryRepository.delete_client(self, id_client_delete)
        self.write_to_file()
        return deleted_client

    def update_client(self, id_client_update, client):

        # """
        # Modifica clientul cu id dat
        # :param if_client_update: int
        # :param client: Client
        # :return: -; clientul cu id-ul dat se modifica, daca exista, atat in fisier cat si in lista curenta
        # :rtype: -;
        # :raises: ValueError daca nu exista client cu id-ul dat
        # """
        ClientInMemoryRepository.update_client(self, id_client_update, client)
        self.write_to_file()


    def find_client(self, id_client_find):
        """
        Cauta client dupa id
        :param id_client: int
        :return: obiectul cu id ul introdus sau exceptia
        """
        return ClientInMemoryRepository.find_client(self, id_client_find)

    def get_all(self):
        """
        Returneaza toti clientii
        :return: dictionar
        """
        return ClientInMemoryRepository.get_all(self)

    def size_clienti(self):
        return ClientInMemoryRepository.size_clienti(self)
