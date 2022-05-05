class Sessao:
    __arranjoCadeiras = []
    def __init__(self, nomeFilme, data, hora):
        self.__nomeFilme = nomeFilme
        self.__data = data
        self.__hora = hora

    def getNomeFilme(self):
        return self.__nomeFilme
    
    def setNomeFilme(self, nome):
        self.__nomeFilme = nome

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getHora(self):
        return self.__hora

    def setHora(self, hora):
        self.__hora = hora

    def getArranjoCadeiras(self):
        return self.__arranjoCadeiras

    def setArranjoDeCadeiras(self, arranjo):
        self.__arranjoCadeiras = arranjo
    
    def ocuparCadeira(self, fila, cadeira):
        self.__arranjoCadeiras[fila][cadeira] = True