from service.film_service import FilmService
from service.client_service import ClientService
from service.inchiriere_service import InchiriereService
class ui:

    def __init__(self,  FilmService, ClientService, InchiriereService):
        self.__film_service = FilmService
        self.__client_service = ClientService
        self.__inchiriere_service = InchiriereService
        self.__comanda = {
            "adauga_film": self.__add_film_ui,
            "print_filme": self.__print_filme_ui,
            "adauga_client": self.__add_client_ui,
            "print_clienti": self.__print_clienti_ui,
            "delete_film": self.__delete_film_ui,
            "delete_cleint": self.__delete_client_ui,
            "find_film": self.__find_film_ui,
            "find_client": self.__find_client_ui,
            "update_film": self.__update_film_ui,
            "update_client": self.__update_client_ui,
            "genereaza_filme": self.__genereaza_filme_ui,
            "genereaza_clienti": self.__genereaza_clienti_ui,
            "adauga_inchiriere": self.__add_inchiriere_ui,
            "adauga_returnare": self.__add_returnare_ui,
            "print_inchirieri": self.__print_inchirieri_ui,
            "print_clienti_nr_filme_inchriate": self.__print_clienti_nr_filme_inchiriate,
            "print_clienti_nume_filme_inchiriate": self.__print_clienti_nume_filme_inchiriate,
            "print_filme_inchiriate": self.__print_filme_inchiriate,
            "print_clienti_nr_filme_inchriate_procent": self.__print_clienti_nr_filme_inchriate_procent,
            "print_ultimele_filme": self.__print_ultimele_filme,
            "print_meniu": self.__printeaza_comenzi
        }
    def __add_film_ui(self, parametrii_add):
        if len(parametrii_add) != 4:
            print("numar de parametrii pentru adaugare film invalid")
            return
        try:
            id_film = int(parametrii_add[0])
            titlu = parametrii_add[1]
            descriere = parametrii_add[2]
            gen = parametrii_add[3]
        except ValueError:
            raise Exception("Parametrii filmului nu respecta tipul cerut")
        self.__film_service.add_film(id_film, titlu, descriere, gen)
        print("Film introdus cu succes")

    def __print_filme_ui(self, parametrii_print):
        if len(parametrii_print) != 0:
            print("numar de parametrii pentru print filme invalid")
            return
        film_stocare = self.__film_service.get_all_filme()
        for film in film_stocare:
            print(film)

    def __delete_film_ui(self, parametrii_delete):
        if len(parametrii_delete) != 1:
            print("numar de parametrii pentru stergere film invalid")
            return
        try:
            id_film_delete = int(parametrii_delete[0])
        except ValueError:
            raise Exception("ID-ul filmului nu respecta tipul cerut")
        self.__film_service.delete_film(id_film_delete)
        print("Film eliminat cu succes")

    def __find_film_ui(self, parametrii_find):
        if len(parametrii_find) != 1:
            print("numar de parametrii pentru cautare film invalid")
            return
        try:
            id_film_find = int(parametrii_find[0])
        except ValueError:
            raise Exception("ID-ul filmului nu respecta tipul cerut")
        print(self.__film_service.find_film(id_film_find))

    def __update_film_ui(self, parametrii_update):
        if len(parametrii_update) != 4:
            print("numar de parametrii pentru modificare film invalid")
            return
        try:
            id_film_update = int(parametrii_update[0])
            titlu_nou = parametrii_update[1]
            descriere_nou = parametrii_update[2]
            gen_nou = parametrii_update[3]
        except ValueError:
            raise Exception("ID-ul filmului nu respecta tipul cerul")
        self.__film_service.update_film(id_film_update, titlu_nou, descriere_nou, gen_nou)
        print("Update realizat cu succes")





    def __add_client_ui(self, parametrii_add):
        if len(parametrii_add) != 3:
            print("numar de parametrii pentru adaugare client invalid")
            return
        try:
            id_client = int(parametrii_add[0])
            nume = parametrii_add[1]
            cnp = parametrii_add[2]
        except ValueError:
            raise Exception("Parametrii clientului nu respecta tipul cerut")
        self.__client_service.add_client(id_client, nume, cnp)
        print("Client introdus cu succes")

    def __print_clienti_ui(self, parametrii_print):
        if len(parametrii_print) != 0:
            print("numar de parametrii pentru print clienti invalid")
            return
        client_stocare = self.__client_service.get_all_clienti()
        for client in client_stocare:
            print(client)

    def __delete_client_ui(self, parametrii_delete):
        if len(parametrii_delete) != 1:
            print("numar de parametrii pentru stergere client invalid")
            return
        try:
            id_client_delete = int(parametrii_delete[0])
        except ValueError:
            raise Exception("ID-ul clientului nu respecta tipul cerut")
        self.__client_service.delete_client(id_client_delete)
        print("Client eliminat cu succes")

    def __find_client_ui(self, parametrii_find):
        if len(parametrii_find) != 1:
            print("numar de parametrii pentru cautare client invalid")
            return
        try:
            id_client_find = int(parametrii_find[0])
        except ValueError:
            raise Exception("ID-ul clientului nu respecta tipul cerut")
        print(self.__client_service.find_client(id_client_find))

    def __update_client_ui(self, parametrii_update):
        if len(parametrii_update) != 3:
            print("numar de parametrii pentru modificare client invalid")
            return
        try:
            id_client_update = int(parametrii_update[0])
            nume_nou = parametrii_update[1]
            cnp_nou = parametrii_update[2]
        except ValueError:
            raise Exception("ID-ul clientului nu respecta tipul cerul")
        self.__client_service.update_client(id_client_update, nume_nou, cnp_nou)
        print("Update realizat cu succes")







    def __add_inchiriere_ui(self, parametrii_inchiriere):
        if len(parametrii_inchiriere) != 3:
            print("numar de parametrii pentru inchiriere client invalid")
            return
        try:
            id_film_inchiriere = int(parametrii_inchiriere[0])
            id_client_inchiriere = int(parametrii_inchiriere[1])
            status_returnare = parametrii_inchiriere[2]
        except ValueError:
            raise Exception("ID-ul nu respecta tipul cerul")
        self.__inchiriere_service.add_inchiriere(id_film_inchiriere, id_client_inchiriere, status_returnare)
        print("Inchirieri inregistrata cu succes")

    def __print_inchirieri_ui(self, parametrii_print):
        if len(parametrii_print) != 0:
            print("numar de parametrii pentru print inchirieri invalid")
            return
        inchirieri = self.__inchiriere_service.get_all_inchirieri()
        for inchiriere in inchirieri:
            print(inchiriere)

    def __add_returnare_ui(self, parametrii_returnare):
        if len(parametrii_returnare) != 3:
            print("numar de parametrii pentru adaugare returnare film invalid")
            return
        try:
            id_film_inchiriere = int(parametrii_returnare[0])
            id_client_inchiriere = int(parametrii_returnare[1])
            status_returnare = parametrii_returnare[2].lower()
        except ValueError:
            raise Exception("ID-ul nu respecta tipul cerul")
        self.__inchiriere_service.add_returnare(id_film_inchiriere, id_client_inchiriere, status_returnare)
        print("Returnare inregistrata cu succes")


    def __print_clienti_nr_filme_inchiriate(self, parametrii):
            if len(parametrii) != 0:
                print("nu puneti alti parametrii")
                return
            lista_clienti  = self.__inchiriere_service.get_clienti_nr_filme_inchiriate_ordonati()
            for client in lista_clienti:
                print(client)

    def __print_clienti_nume_filme_inchiriate(self, parametrii):
        if len(parametrii) != 0:
            print("nu puneti alti parametrii")
            return
        lista_clienti  = self.__inchiriere_service.get_clienti_nr_filme_inchiriate_sortnume()
        for client in lista_clienti:
            print(client)


    def __print_filme_inchiriate(self, parametrii):
        if len(parametrii) != 1:
            print("Nr parametrii incorect")
            return
        try:
            n = int(parametrii[0])
        except ValueError:
            raise Exception("numarul de filme nu resoecta tipul cerut")

        lista_filme  = self.__inchiriere_service.get_filme_nr_clienti_ordonate(n)
        for film in lista_filme:
            print(film)

    def __print_clienti_nr_filme_inchriate_procent(self, parametrii):
        if len(parametrii) != 1:
            print("Nr parametrii incorect")
            return
        try:
            p = int(parametrii[0])
        except ValueError:
            raise Exception("procentul nu resoecta tipul cerut")

        lista_clienti  = self.__inchiriere_service.get_clienti_nr_filme_inchiriate_procent(p)
        for client in lista_clienti:
            print(client)


    def __print_ultimele_filme(self, parametrii):
        if len(parametrii) != 1:
            print("Nr parametrii incorect")
            return
        try:
            n = int(parametrii[0])
        except ValueError:
            raise Exception("numarul de filme nu respectatipul cerut")

        lista_filme  = self.__inchiriere_service.get_filme_nr_inchirieri_mic(n)
        for film in lista_filme:
            print(film)



    def __genereaza_filme_ui(self, parametrii_generare):
        if len(parametrii_generare) != 1:
            print("numar de parametrii pentru generare filme invalid")
            return
        try:
            nr_generare = int(parametrii_generare[0])
        except ValueError:
            raise Exception("nu se respecta tipul int")
        self.__film_service.genereaza_filme(nr_generare)
        print("Filme adaugate cu succes")


    def __genereaza_clienti_ui(self, parametrii_generare):
        if len(parametrii_generare) != 1:
            print("numar de parametrii pentru generare clienti invalid")
            return
        try:
            nr_generare = int(parametrii_generare[0])
        except ValueError:
            raise Exception("nu se respecta tipul int")
        self.__client_service.genereaza_clienti(nr_generare)
        print("Clienti adugati cu succes")


    def __printeaza_comenzi(self, parametrii_printeaza_meniu):
        if len(parametrii_printeaza_meniu) != 0:
            print("nu puneti alti parametrii")
            return
        print("Adauga film             : adauga_film 1 Atonement foarte_bun razboi ")
        print("Afiseaza filme          : print_filme")
        print("Sterge film dupa id     : delete_film 1")
        print("Modifica film dupa id   : update_film 1 Atonement genial drama")
        print("Cautare film dupa id    : find_film 1")

        print("Adauga client           : adauga_client 1 Alexandra 6040235635234")
        print("Afiseaza clienti        : print_clienti")
        print("Sterge client dupa id   : delete_client 1 Ioana 6040235765234")
        print("Modifica client dupa id : update_client 1 Ioana 6040235765234")
        print("Cautare client dupa id  : find_client 1")

        print("Adauga inchiriere       : adauga_inchiriere 2 3 -")
        print("Adauga returnare film   : adauga_returnare 2 3 DA")
        print("Afiseaza inchirierile   : print_inchirieri")
        print("Afiseaza primii clientii ordonati dupa numarul de filme inchiriate : print_clienti_nr_filme_inchriate")
        print("Afiseaza primii clienti cu filme inchiriate ordonati dupa nume     : print_clienti_nume_filme_inchiriate")
        print("Afiseazaa cele mai inchiriate n filme                              : print_filme_inchiriate 2")
        print("Afiseaza primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)  : print_clienti_nr_filme_inchriate_procent 30")
        print("Afiseaza ultimele n filme ca numar de inchirieri                   : print_ultimele_filme 2")

        print("Afiseaza comenzile      : print_meniu")
        print("Exit                    : exit")
        print("Genereaza aleatoriu n filme : genereaza_filme 10")
        print("Genereaza aleatoriu n clienti : genereaza_clienti 10")

    def run(self):
        self.__printeaza_comenzi([])
        while True:
            string_comanda = input("\nIntroduceti comanda    ")
            string_comanda = string_comanda.strip()

            if string_comanda == 'exit':
                break
            lista_comanda = string_comanda.split(" ")
            comanda = lista_comanda[0]
            parametrii = lista_comanda[1:]
            if comanda in self.__comanda:
                try:
                    self.__comanda[comanda](parametrii)
                except Exception as ex:
                    print (ex)
            else:
                print("Comanda invalida")