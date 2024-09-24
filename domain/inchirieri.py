class Inchiriere:

    def __init__(self, id_film, id_client, status_returnare):
        #Daca citim din fisier, citim doar id-ri (cnp-ri), nu toate datele obiectului
        self.__id_film = id_film
        self.__id_client = id_client
        self.__status_returnare = status_returnare

    def get_id_film(self):
        return self.__id_film

    def get_id_client(self):
        return self.__id_client

    def get_status_returnare(self):
        return self.__status_returnare

    def __eq__(self, other):
        return self.__id_client == other.get_id_client() and self.__id_film == other.get_id_film()

    def __str__(self):
        return 'ID film: ' + str(self.__id_film) + ' | ID clent: ' + str(self.__id_client) +  ' | status returnare: '  + str(self.__status_returnare)











#CLASA PENTRU CITIREA DIN MEMORIE (retinem OBIECTUL client, OBIECTUL film si statusul
#
#class Inchiriere:
#     """
#     Clasa de legătură: 1 client poate inchirira 1 sau mai multe filme
#                        1 film poate fi inchiriat de 1 sau mai multe persoane
#     Atribute:
#         --necesar pentru a gestiona: filme, clienti
#         --evaluare: string - 'da' sau '-'
#     """
#
#     def __init__(self, film, client, status_returnare):
#         self.__film = film
#         self.__client = client
#         self.__status_returnare = status_returnare
#
#     def get_film(self):
#         return self.__film
#
#     def get_client(self):
#         return self.__client
#
#     def get_returnare(self):
#         return self.__status_returnare
#
#     def __eq__(self, other):
#         return self.__client == other.get_client() and self.__film == other.get_film()
#
#     def __str__(self):
#         return str(self.__film) + '   -->   ' + str(self.__client) + '   -->   Returnat' + str(self.__status_returnare)