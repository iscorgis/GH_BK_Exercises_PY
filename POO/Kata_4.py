
class Animal():
    #Properties
    __especie = ''
    __peso = 0
    __altura = 0.0

    #methods
    def __init__(self,especie,peso,altura):
        self.__especie = especie
        self.__peso = peso
        self.__altura = altura

    #getters / setters
    #Investigar decoradores

    def get_especie(self):
        pass
    def get_peso(self):
        pass
    def get_altura(self):
        pass

    def set_especie(self,especie):
        self.__especie = especie
    def set_peso(self,peso):
        self.__peso = peso
    def set_altura(self,altura):
        self.__altura = altura

    def comer(self):
        print('Estoy comiendo')

    def cazar(self):
        print('Voy a dormir')

    def dormir(self):
        print('Voy a dormir')


class Leon(Animal):

    def __init__(self,altura, peso):
        super().__init__('Leon',altura,peso)

class Mascota():
    __nombre = ''
    __dueño = ''

    def __init__(self,nombre, dueño):
        self.__nombre = nombre
        self.__dueño = dueño

    def sentarse(self):
        print('Me siento')


class Perro(Animal,Mascota):

    def __init__(self,nombre,dueño,altura, peso):
       Animal.__init__('Perro', altura, peso)
       Mascota.__init__(nombre,dueño)

Kali = Perro('Kali','Manu',0.5,25)
Kali.cazar()
Kali.sentarse()
print()




