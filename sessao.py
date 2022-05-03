class Sessao:
    def __init__(self, nomeFilme, duracaoFilme):
        self.__nomeFilme = nomeFilme
        self.__duracaoFilme = duracaoFilme

    def getNomeFilme(self):
        return self.__nomeFilme
    
    def setNomeFilme(self, nome):
        self.__nomeFilme = nome

    def getDuracaoFilme(self):
        return self.__duracaoFilme

    def setDuracaoFilme(self, duracaoFilme):
        self.__duracaoFilme = duracaoFilme