class Sala:
    def __init__(self, numero, filme, sessoes, filas, cadeiras):
        self.__numero = numero
        self.__filme = filme
        self.__sessoes = sessoes
        self.__arranjoCadeiras = self.__gerarCadeira(filas, cadeiras)
        self.__filas = filas
        self.__cadeiras = cadeiras
    
    def __gerarCadeiras(self, filas, cadeiras):
      return [[{ocupado: False}] * filas for _ in range(cadeiras)]