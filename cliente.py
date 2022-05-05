class Cliente:
    __reservas = []

    def __init__(self, numeroTelefone):
        self.__numeroTelefone = numeroTelefone
    
    def getNumeroTelefone(self):
        return self.__numeroTelefone
    
    def setNumeroTelefone(self, numeroTelefone):
        self.__numeroTelefone = numeroTelefone
    
    def adicionarReservas(self, reserva):
        self.__reservas.append(reserva)
    
    def imprimirReservas(self):
        for reserva in self.__reservas:
            reserva.imprimir()