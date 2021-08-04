
class Serie():
    # Properties

    __Titulo          = ''
    __Num_temporadas  = 3
    __Entregado       = False
    __Genero          = ''
    __Creador         = ''

    #Constructor
    def __init__(self, titulo, num_temporadas, entregado, genero, creador):
        self.__Titulo           = titulo
        self.__Num_temporadas   = num_temporadas
        self.__Entregado        = entregado
        self.__Genero           = genero
        self.__Creador          = creador

    def get_Titulo(self):
        return self.__Titulo

    def get_Num_temporadas(self):
        return self.__Num_temporadas

    def get_Genero(self):
        return self.__Genero


    def get_Creador(self):
        return self.__Creadora

    def set_Titulo(self, titulo):
         self.__Titulo = titulo


    def set_Num_temporadas(self, num_temporadas):
         self.__Num_temporadas= num_temporadas


    def set_Genero(self, genero):
         self.__Genero = genero

    def set_Creador(self, creador):
         self.__Creadora = creador

    def __str__(self):
        return "La serie {0} consta de {1} temporadas".format(self.__Titulo, self.__Num_temporadas)



