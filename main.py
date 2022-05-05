from reserva import Reserva
from cliente import Cliente
from reservaCliente import ReservaCliente
from reservaSala import ReservaSala
from sala import Sala
from sessao import Sessao

sessao1 = Sessao("Impuros", "19/04", "15h")
sessao2 = Sessao("Puros",  "20/04", "20h")
sessao3 = Sessao("Lavados", "21/04", "19h")

sala1 = Sala(1, sessao1, 4, 10)
sala2 = Sala(2, sessao2, 5, 10)
sala3 = Sala(3, sessao3, 6, 10)

