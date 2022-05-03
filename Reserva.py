class Reserva:
    __reservas = []

    
    def __init__(self, sala, filme, dia, sessao):
        self.__sala = sala
        self.__filme = filme
        self.__dia = dia
        self.__sessao = sessao
    
    def getSala(self):
        return self.__sala

    def getFilme(self):
        return self.__filme

    def getDia(self):
        return self.__dia

    def getSessao(self):
        return self.__sessao

    def setSala(self, sala):
        self.__sala = sala
    
    def setFilme(self, filme):
        self.__filme = filme

    def setDia(self, dia):
        self.__dia = dia

    def setSessao(self, sessao):
        self.__sessao = sessao

    
