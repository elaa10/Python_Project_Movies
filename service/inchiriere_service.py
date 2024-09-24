from domain.inchirieri import Inchiriere
from domain.dtos import ClientInchiriere, FilmInchiriere

class InchiriereService:

    def __init__(self, repo_inchiriere, validator_inchiriere, repo_film, repo_client):
        self.__repo_inchiriere = repo_inchiriere
        self.__validator_inchiriere = validator_inchiriere
        self.__repo_film = repo_film
        self.__repo_client = repo_client

    def add_inchiriere(self, id_film_inchiriere, id_client_inchiriere, status_returnare):
        """
                Verifica daca exista o inchiriere cu id-rile date, creza noul obiect inchiriere si apeleaza add returnare din repo pt updatarea efectiva
                :param id_film_inchiriere: int
                :param id_client_inchiriere: int
                :param status_returnare: string
                return: -
        """

        try:
            film = self.__repo_film.find_film(id_film_inchiriere)
        except Exception:
            raise ValueError("Nu exista film cu id-ul dat")

        try:
            client = self.__repo_client.find_client(id_client_inchiriere)
        except Exception:
            raise ValueError("Nu exista client cu id-ul dat")

        self.__validator_inchiriere.valideaza_status_inchiriere(status_returnare)
        inchiriere = Inchiriere(id_film_inchiriere, id_client_inchiriere, status_returnare)
        self.__repo_inchiriere.add_inchiriere(inchiriere)


    def add_returnare(self, id_film_inchiriere, id_client_inchiriere, status_returnare):
        """
        <=> update inchiriere
        Creza o inchiriere si apeleaza add din repo pt adaugarea efectiva
        :param id_film_inchiriere: int
        :param id_client_inchiriere: int
        :param status_returnare: string
        return: -
        """
        #verificam daca exista id film introdus
        try:
            film = self.__repo_film.find_film(id_film_inchiriere)
        except Exception:
            raise ValueError("Nu exista film cu id-ul dat")

        # verificam daca exista id client introdus
        try:
            client = self.__repo_client.find_client(id_client_inchiriere)
        except Exception:
            raise ValueError("Nu exista client cu id-ul dat")


        #verificam daca exista o astfel de inchiriere
        inchiriere = Inchiriere(id_film_inchiriere, id_client_inchiriere, status_returnare)
        try:
            index_inchiriere_de_inlocuit = self.__repo_inchiriere.get_all().index(self.__repo_inchiriere.find_inchiriere(inchiriere))
        except Exception:
            raise ValueError("Nu exista o astfel de inchiriere")

        self.__validator_inchiriere.valideaza_status_returnare(status_returnare)
        self.__repo_inchiriere.add_returnare(index_inchiriere_de_inlocuit, inchiriere)


    def quickSort(self, list, key=None, reverse=False):
        """
        Ordoneaza lista folosind metoda quick sort (folosim list comprehension)
        :return: lista ordonata
        :rtype: list
        """
        if len(list) <= 1:
            return list
        pivot = list.pop()
        lesser = [x for x in list if (key(x) if key else x) < (key(pivot) if key else pivot)]
        greater = [x for x in list if (key(x) if key else x) >= (key(pivot) if key else pivot)]

        # lesser = [x for x in list if key(x) <= key(pivot) if key else x <= pivot)] dar mie imi apare eroare la aceasta scriere

        if reverse:
            return self.quickSort(greater, key=key, reverse=True) + [pivot] + self.quickSort(lesser, key=key, reverse=True)
        else:
            return self.quickSort(lesser, key=key) + [pivot] + self.quickSort(greater, key=key)


    def gnome_sort(self, list, key=None, reverse=False):

        index = 0
        while index < len(list):
            if key:
                # Comparam elemntele folosind key
                if index == 0 or key(list[index]) >= key(list[index - 1]):
                    index += 1
                else:
                    list[index], list[index - 1] = list[index - 1], list[index]
                    index -= 1
            else:
                # Comparam elementele simplu, daca nu avem key
                if index == 0 or list[index] >= list[index - 1]:
                    index += 1
                else:
                    list[index], list[index - 1] = list[index - 1], list[index]
                    index -= 1

        if reverse:
            return list[::-1]
        return list

#pentru valori egale gnome_sort si quick sort pune aceste numere pe pzitii diferite pt reverse=True
#pt reverse=True testele merg pt quick sort (ar trebui sa schimb intre ele valorile egale pt gnome sort)

    def get_clienti_nr_filme_inchiriate_ordonati(self):
        """
        Returneaza clientii ordonati dupa nr de filme inchiriate (descrescator)
        :return: lista de DTOs care contin informatiile necesare
        :rtype: list
        """
        dto_list = self.__repo_inchiriere.get_clienti_nr_filme()
        dto_list = self.quickSort(dto_list, key=lambda item: item.get_nr_inchirieri(), reverse=True)


        #clienti_cele_mai_multe_filme_inchiriate_n = dto_list[:n]
        for client_dto in dto_list:
            id_client = client_dto.get_id_client()
            client_obiect = self.__repo_client.find_client(id_client)
            client_dto.set_nume(client_obiect.get_nume())
            client_dto.set_cnp(client_obiect.get_cnp())



        return dto_list


    def get_clienti_nr_filme_inchiriate_sortnume(self):
        """
        Returneaza clientii cu filme inchiriate ordonati dupa nume
        :return: lista de DTOs care contin informatiile necesare
        :rtype: list
        """
        dto_list = self.__repo_inchiriere.get_clienti_nr_filme()
        for client_dto in dto_list:
            id_client = client_dto.get_id_client()
            client_obiect = self.__repo_client.find_client(id_client)
            client_dto.set_nume(client_obiect.get_nume())
            client_dto.set_cnp(client_obiect.get_cnp())

        dto_list = self.quickSort(dto_list, key=lambda item: (item.get_nume(), item.get_nr_inchirieri()))

        return dto_list


    def get_filme_nr_clienti_ordonate(self, n):
        """
        Returneaza primele n filme ordonate dupa nr de clienti  (descrescator)
        :return: lista de DTOs care contin informatiile necesare
        :rtype: list
        """
        dto_list = self.__repo_inchiriere.get_filme_nr_clienti()
        dto_list = self.quickSort(dto_list, key=lambda item: item.get_nr_clienti(), reverse=True)


        primele_n_filme = dto_list[:n]
        for film_dto in primele_n_filme:
            id_film = film_dto.get_id_film()
            film_obiect = self.__repo_film.find_film(id_film)
            film_dto.set_titlu(film_obiect.get_titlu())
            film_dto.set_descriere(film_obiect.get_descriere())
            film_dto.set_gen(film_obiect.get_gen())

        return primele_n_filme



    def get_filme_nr_inchirieri_mic(self, n):
        """
        Returneaza  ultimele n filme dupa nr de clienti
        :return: lista de DTOs care contin informatiile necesare
        :rtype: list
        """
        dto_list = self.__repo_inchiriere.get_filme_nr_clienti()
        dto_list = self.gnome_sort(dto_list, key=lambda item: item.get_nr_clienti())

        ultimele_n_filme = dto_list[:n]
        for film_dto in ultimele_n_filme:
            id_film = film_dto.get_id_film()
            film_obiect = self.__repo_film.find_film(id_film)
            film_dto.set_titlu(film_obiect.get_titlu())
            film_dto.set_descriere(film_obiect.get_descriere())
            film_dto.set_gen(film_obiect.get_gen())

        return ultimele_n_filme



    def get_clienti_nr_filme_inchiriate_procent(self, p):
        """
                Returneaza primii x% clienti ordonati dupa nr de filme inchiriate (descrescator)
                :return: lista de DTOs care contin informatiile necesare
                :rtype: list
        """
        dto_list = self.__repo_inchiriere.get_clienti_nr_filme_simplu()
        dto_list = self.quickSort(dto_list, key=lambda item: item.get_nr_inchirieri(), reverse=True)

        n = int((p / 100) * len(dto_list))
        primii_n_clienti = dto_list[:n]
        for client_dto in primii_n_clienti:
            id_client = client_dto.get_id_client()
            client_obiect = self.__repo_client.find_client(id_client)
            client_dto.set_nume(client_obiect.get_nume())

        return primii_n_clienti


    def get_all_inchirieri(self):
        """
               Returneaza lista cu toate inchirierile
        """
        return self.__repo_inchiriere.get_all()



