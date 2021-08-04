
class Alumno():
    # Properties

    Nombre = ''
    Apellido = ''
    Dni = ''
    Edad = 0
    asignatura = []

    def __init__(self,nombre,apellido,dni,edad,nota):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Dni = dni
        self.Edad = edad


    # Methonds()

    def Saludar(self):
        print('Hola soy {0} {1}'.format(self.nombre,self.Apellido))
        #print(f'Hola, me llamo {self.nombre}')

    def AnadirNota(self,nota):
        self.Nota = nota

    def CumplirAnos(self):
        self.Edad += 1


class Asignatura():
    nombre = ''
    nota = 0

    def __init__(self,nombre):
        self.nombre = nombre

    def AnadirNota(self, nota):
        self.Nota = nota