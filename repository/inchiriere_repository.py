from domain.inchirieri import Inchiriere
from domain.dtos import ClientInchiriere, FilmInchiriere, ClientInchiriereSimplu

class InchiriereInMemoryRepository:

    def __init__(self):
        self.__inchiriere_stocare = []


    def add_inchiriere(self, inchiriere):
        """
            Adauga inchirierea data
            :param inchiriere: obiect
            :return: -; inchirierea este adaugata la sfarsitul listei de inchirieri
            :raises: ValueError daca mai exista o inchiriere identica
        """

        if self.find_inchiriere(inchiriere) is not None:
            raise ValueError("Exista deja aceasta inchiriere.")
        self.__inchiriere_stocare.append(inchiriere)


    def find_inchiriere(self, inchiriere):
        """
                Cauta inchirierea data in lista
                :param inchiriere: obiect
                :return: inchirierea gasita daca aceasta exista, None altfel
        """
        for inchiriere_curenta in self.__inchiriere_stocare:
            if inchiriere_curenta == inchiriere:
                return inchiriere
        return None

    def add_returnare(self, index, inchiriere):
        """
        Modifica(update) statusul returnaarii
        :param inchiriere: obiect
        :return: - sau exception
        """
        self.__inchiriere_stocare[index] = inchiriere

    def get_all(self):
        return self.__inchiriere_stocare

    def size_inchirieri(self):
        return len(self.get_all())





class InchiriereFileRepository(InchiriereInMemoryRepository):

    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.read_from_file()


    def read_from_file(self):
        """
        Citeste inchirierile din fisier
        :retunr: -; incarca inchirierile
        """
        with open(self.__filename, 'r') as filme_file:
            lines = filme_file.readlines()
            lines = [line.strip() for line in lines if line.strip() != '']
            for line in lines:
                id_film, id_client, status_returnare = line.split(',')
                id_film = int(id_film.strip())
                id_client = int(id_client.strip())
                status_returnare = status_returnare.strip()
                inchiriere = Inchiriere(id_film, id_client, status_returnare)
                super().add_inchiriere(inchiriere)

    def write_to_file(self):
        """
        Salveaza in fisier inchirierile curente
        """
        inchirieri = super().get_all()
        with open(self.__filename, 'w') as inchirieri_file:
            for inchiriere in inchirieri:
                line_to_write = str(inchiriere.get_id_film()) + ',' + str(inchiriere.get_id_client()) + ',' + str(str(inchiriere.get_status_returnare())  + '\n')
                inchirieri_file.write(line_to_write)


    def add_inchiriere(self, inchiriere):
        """
        Adauga inchiriere data
        :param inchiriere: inchiriere de adaugat
        :type inchiriere: Inchiriere
        :return: -; inchirierea este adugata la sfarsitul listei de inchirieri
        """
        super().add_inchiriere(inchiriere)
        self.write_to_file()

    def add_returnare(self, index, inchiriere):
        """
        Modifica(update) statusul returnaarii
        :param index: indexul obiectului inchiriere din dictionarul dat
        :param inchiriere: obiect
        :return: - sau exception
        """
        super().add_returnare(index, inchiriere)
        self.write_to_file()


    def find_inchiriere(self, inchiriere):
        """
                Cauta inchirierea data in lista
                :param inchiriere: obiect
                :return: inchirierea gasita daca aceasta exista, None altfel
        """
        return super().find_inchiriere(inchiriere)

    def get_clienti_nr_filme(self):
        """
        Returneaza o lista de obiecte dto ClientInchiriere ce contin informatii despre client si nr de filme inchiriate
        :return: lista de dto
        :rtype: list
        """
        clienti_dict = {}
        inchirieri = self.get_all()
        for inchiriere in inchirieri:
            current_id_client = inchiriere.get_id_client()
            if current_id_client in clienti_dict:
                clienti_dict[current_id_client].increase_nr_inchirieri()
            else:
                clienti_dict[current_id_client] = ClientInchiriere(inchiriere.get_id_client())
        return list(clienti_dict.values())

    def get_filme_nr_clienti(self):
        """
        Returneaza o lista de obiecte dto FilmInchiriere ce contin informatii despre film si nr de inchirieri
        :return: lista de dto
        :rtype: list
        """

        filme_dict = {}
        inchirieri = self.get_all()
        for inchiriere in inchirieri:
            current_id_film = inchiriere.get_id_film()
            if current_id_film in filme_dict:
                filme_dict[current_id_film].increase_nr_clienti()
            else:
                filme_dict[current_id_film] = FilmInchiriere(inchiriere.get_id_film())
        return list(filme_dict.values())

    def get_clienti_nr_filme_simplu(self):
        """
        Returneaza o lista de obiecte dto ClientInchiriereSimplu ce contin id-ul si nuumele  clientului si nr de filme inchiriate
        :return: lista de dto
        :rtype: list
        """
        clienti_dict = {}
        inchirieri = self.get_all()
        for inchiriere in inchirieri:
            current_id_client = inchiriere.get_id_client()
            if current_id_client in clienti_dict:
                clienti_dict[current_id_client].increase_nr_inchirieri()
            else:
                clienti_dict[current_id_client] = ClientInchiriereSimplu(inchiriere.get_id_client())
        return list(clienti_dict.values())


    def get_all(self):
        return super().get_all()

    def size_inchirieri(self):
        return super().size_inchirieri()






