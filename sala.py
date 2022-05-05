class Sala:
    __sessoes = []
    __reservas = []
    def __init__(self, numero, filas, cadeiras):
        self.__numero = numero
        self.__arranjoCadeiras = self.__gerarCadeiras(filas, cadeiras)
        self.__filas = filas
        self.__cadeiras = cadeiras
    
    def __gerarCadeiras(self, filas, cadeiras):
      return [[False] * filas for _ in range(cadeiras)]

    def getNumero(self):
        return self.__numero

    def getSessoes(self):
        return self.__sessoes

    def getArranjoCadeiras(self):
        return self.__arranjoCadeiras

    def getFilas(self):
        return self.__filas
    
    def getCadeiras(self):
        return self.__cadeiras

    def getReservas(self):
        return self.__reservas

    def setNumero(self, numero):
        self.__numero = numero

    def setFilas(self, filas):
        self.__filas = filas
        self.__gerarCadeiras(self.__filas, self.__cadeiras)

    def setCadeiras(self, cadeiras):
        self.__cadeiras = cadeiras
        self.__gerarCadeiras(self.__cadeiras, self.__cadeiras)

    def adicionarSessao(self, sessao):
        sessaoCopy = sessao
        sessaoCopy.getArranjoCadeiras = self.__arranjoCadeiras
        self.__sessoes.append(sessaoCopy)
    
    def removerSessao(self, sessao):
        self.__sessoes.remove(sessao)

    def adicionarReserva(self, reserva):
        self.__reservas.append(reserva)

    
    
