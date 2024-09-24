class ValidatorFilm:

    def __init__(self):
        pass

    def valideaza_film(self, film):
        """
                Valideaza un film dat
                :param film: filmul care se valideaza
                :return: -
                :raises: ValueError daca filmul nu e valid
        """
        erori = []
        if film.get_id_film() < 0:
            erori.append("id invalid")

        if len(erori) > 0:
            raise Exception(erori)


class ValidatorClient:

    def __init__(self):
        pass

    def valideaza_client(self, client):
        """
                Valideaza un client dat
                :param client: clientul care se valideaza
                :return: -
                :raises: ValueError daca clientul nu e valid
        """
        erori = []
        if client.get_id_client() < 0:
            erori.append("id inavalid")
        if len(client.get_cnp()) != 13:
            erori.append("cnp invalid ")
        if len(erori) > 0:
            raise Exception(erori)

class ValidatorInchiriere:

    def __init__(self):
        pass

    def valideaza_status_inchiriere(self, status):
        """
                Valideaza statusul inchirierii (el trebuie sa fie mereu '-')
                :param status: string
                :return: -
                :raises: ValueError daca statusul nu e valid
        """
        erori = []
        if status != '-':
            erori.append("La inchirieri status trebuie sa fie mereu '-")
        if len(erori) > 0:
            raise Exception(erori)


    def valideaza_status_returnare(self, status):
        """
                Valideaza statusul introdus pt returnare (el trebuie sa fie 'da')
                :param status: string
                :return: -
                :raises: ValueError daca statusul nu e valid
        """
        erori = []
        if status != 'da':
            erori.append("La returnare status trebuie sa fie 'da")
        if len(erori) > 0:
            raise Exception(erori)

