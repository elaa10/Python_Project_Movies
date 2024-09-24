from UI import *
from domain.validator import ValidatorFilm, ValidatorClient,ValidatorInchiriere

from repository.film_repository import FilmFileRepository, FilmInMemoryRepository
from repository.client_repository import ClientInMemoryRepository, ClientFileRepository
from repository.inchiriere_repository import InchiriereInMemoryRepository, InchiriereFileRepository

from service.film_service import FilmService
from service.client_service import ClientService
from service.inchiriere_service import InchiriereService


repo_film = FilmFileRepository("data/filme.txt")
validator_film = ValidatorFilm()
service_film = FilmService(repo_film, validator_film)

repo_client = ClientFileRepository("data/clienti.txt")
validator_client = ValidatorClient()
service_client = ClientService(repo_client, validator_client)

repo_inchiriere = InchiriereFileRepository("data/inchirieri.txt")
validator_inchiriere = ValidatorInchiriere()
service_inchiriere = InchiriereService(repo_inchiriere, validator_inchiriere, repo_film, repo_client)

console = ui(service_film, service_client, service_inchiriere)
console.run()


# am implementat recursiv funciitle    genereaza_filme din film_service    si   genereaza_clienti din client_service;
# au cmplexitatea(overall complexity) teta(n)?



# este implementat recursiv si quickSort din inchiriere_service
#  ANALIZA COMPLEXITATII:
#  Caz favorabil: pivotul este exact la mijloc (nr mai mici ca pivotul=nr mai mari ca pivotul)   comlexitatea teta(n*log2n)
#  Caz defavorabil: partitionarea rezulta intr-o partitie cu 1 element si n-1 elemente           complexitatea teta(n^2)
#  Average:  complexitatea teta(n*log2n)
