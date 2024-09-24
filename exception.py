class RepositoryException(Exception):
    def __init__(self, msg):
       self.__msg = msg

    def __str__(self):
        return "Repository exception:" + str(self.__msg)

class NuExistaAcestIdFilmException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Nu exista id film introdus")