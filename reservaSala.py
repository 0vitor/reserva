from reserva import Reserva

class ReservaSala(Reserva):
    def __init__(self, sala, dia, sessao, fila, cadeira, telefone):
        Reserva.__init__(self, sala, dia, sessao, fila, cadeira)
        self.__telefone = telefone

    def getTelefone(self):
        return self.__telefone
    
    def setTelefone(self, telefone):
        self.__telefone = telefone

    def imprimir(self):
        print(f'sala: {self.__sala}, filme: {self.__filme}, sessao: {self.__sessao}, fila: {self.__fila}, cadeira: {self.__cadeira}, telefone: {self.__telefone}')