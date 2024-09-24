class ClientInchiriere:
    def __init__(self, id_client):
        self.__id_client = id_client
        self.__nume = ""
        self.__cnp = ""
        self.__nr_inchirieri = 1

    def get_id_client(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume

    def set_nume(self, nume):
        self.__nume = nume

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def increase_nr_inchirieri(self):
        self.__nr_inchirieri +=1

    def get_nr_inchirieri(self):
        return self.__nr_inchirieri

    def __str__(self):
        return "ID: " + str(self.get_id_client()) + " | " + "Nume: " + self.get_nume() + " | " + "CNP: " + self.get_cnp() + "  ----> nr filme inchiriate  " + str(self.get_nr_inchirieri())



class FilmInchiriere:
    def __init__(self, id_film):
        self.__id_film = id_film
        self.__titlu = ""
        self.__descriere = ""
        self.__gen = ""
        self.__nr_clienti = 1

    def get_id_film(self):
        return self.__id_film

    def get_titlu(self):
        return self.__titlu

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def get_descriere(self):
        return self.__descriere

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def get_gen(self):
        return self.__gen

    def set_gen(self, gen):
        self.__gen = gen

    def increase_nr_clienti(self):
        self.__nr_clienti +=1

    def get_nr_clienti(self):
        return self.__nr_clienti

    def __str__(self):
        return   "ID: " + str(self.get_id_film()) + " | " + "Titlu: " + self.get_titlu() + " | " + "Descriere: " + self.get_descriere() + " | " + "Gen: " + self.get_gen() + "  ----> nr clienti  " + str(self.get_nr_clienti())



class ClientInchiriereSimplu:
    def __init__(self, id_client):
        self.__id_client = id_client
        self.__nume = ""
        self.__nr_inchirieri = 1

    def get_id_client(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume

    def set_nume(self, nume):
        self.__nume = nume

    def increase_nr_inchirieri(self):
        self.__nr_inchirieri +=1

    def get_nr_inchirieri(self):
        return self.__nr_inchirieri

    def __str__(self):
        return  "Nume: " + self.get_nume() +  "  ----> nr filme inchiriate  " + str(self.get_nr_inchirieri())