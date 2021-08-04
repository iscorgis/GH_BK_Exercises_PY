

from Serie import Serie
from Videojuego import Videojuego

class Entregable(Serie,  Videojuego):

    __prestado = False

    def __init__(self, tipo, titulo, duracion, entregado, genero, creador ):
        #if tipo == 'Serie':
        Serie.__init__(self, titulo, duracion, entregado, genero, creador)
        #if tipo == 'Videojuego':
        Videojuego.__init__(self, titulo, duracion, entregado, genero, creador)

    def entregar(self):
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

    def isEntregado(self):
        return self.__prestado

    def compareTo(self, object) :
        return self.__dict__ == object.__dict__

