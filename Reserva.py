class Reserva:

    def __init__(self, sala, sessao, fila, cadeira):
        self.__sala = sala
        self.__sessao = sessao
        self.__fila = fila
        self.__cadeira = cadeira

    def imprimir(self):
        print(f'sala: {self.__sala}, filme: {self.__filme}, sessao: {self.__sessao}, fila: {self.__fila}, cadeira: {self.__cadeira}')

    def getSala(self):
        return self.__sala

    def getFilme(self):
        return self.__filme

    def getDia(self):
        return self.__dia

    def getFila(self):
        return self.__fila

    def getCadeira(self):
        return self.__cadeira

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

    
