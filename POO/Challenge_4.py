

class Serie():
    # Properties

    __Titulo          = ''
    __Num_temporadas  = 3
    __Entregado       = False
    __Genero          = ''
    __Creador         = ''

    #Constructor
    def __init__(self,nombre,apellido,dni,edad,nota):
        self.__Titulo           = nombre
        self.__Num_temporadas   = apellido
        self.__Entregado        = dni
        self.__Genero           = edad
        self.__Creador          = nota

    #@property
    def get_Titulo(self):
        return self.__Titulo

    def get_Num_temporadas(self):
        return self.__Num_temporadas

    def get_Entregado(self):
        return self.__Entregado

    def get_Genero(self):
        return self.__Genero

    def get_Creador(self):
        return self.__Creadora

    #@property.setter
    def set_(self, nombre):
        self.__