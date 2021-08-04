class Videojuego():

    __Titulo            = ''
    __Horas_estimadas  = 10
    __Entregado         = False
    __Genero            = ''
    __Compania          = ''

    #Constructor
    def __init__(self, titulo, horas_estimadas, entregado, genero, compania):
        self.__Titulo           = titulo
        self.__Horas_estimadas   = horas_estimadas
        self.__Entregado        = entregado
        self.__Genero           = genero
        self.__Compania          = compania

    def get_TituloV(self):
        return self.__Titulo

    def get_Horas_Estimadas(self):
        return self.__Horas_estimadas

    def get_Genero(self):
        return self.__Genero

    def get_Compania(self):
        return self.get_Compania

    def set_TituloV(self, titulo):
         self.__Titulo = titulo


    def set_Horas_Estimadas(self, horas_estimadas):
         self.__Num_temporadas= horas_estimadas


    def set_Genero(self, genero):
         self.__Genero = genero

    def set_Compania(self, compania):
         self.__Compania= compania

    def __str__(self):
        return "El videojuego {0} tiene {1} horas estimadas".format(self.get_Titulo, self.get_Horas_Estimadas)
