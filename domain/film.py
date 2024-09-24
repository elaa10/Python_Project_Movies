class Film:

    def __init__(self, id_film, titlu, descriere, gen):
        self.__atribute = [id_film, titlu, descriere, gen]

    def get_id_film(self):
        return self.__atribute[0]

    def get_titlu(self):
        return self.__atribute[1]

    def get_descriere(self):
        return self.__atribute[2]

    def get_gen(self):
        return self.__atribute[3]

    def set_id_film(self, id_nou):
        self.__atribute[0] = id_nou

    def set_titlu(self, titlu_nou):
        self.__atribute[1] = titlu_nou

    def set_descriere(self, descriere_nou):
        self.__atribute[2] = descriere_nou

    def set_gen(self, gen_nou):
        self.__atribute[3] = gen_nou

    def __eq__(self, film_verif):
        return self.__atribute[0] == film_verif.__atribute[0]

    def  __str__(self):
        return "ID: " + str(self.get_id_film()) + " | " + "Titlu: " + self.get_titlu() + " | " + "Descriere: " + self.get_descriere() + " | " + "Gen: " + self.get_gen()
