
class Alumno():
    # Properties

    Nombre = ''
    Apellido = ''
    Dni = ''
    Edad = 0
    Nota = 0

    def __init__(self,nombre,apellido,dni,edad,nota):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Dni = dni
        self.Edad = edad
        self.Nota = nota

    # Methonds()

    def Saludar(self):
        print('Hola soy {0} {1}'.format(self.nombre,self.Apellido))
        #print(f'Hola, me llamo {self.nombre}')

    def AnadirNota(self,nota):
        self.Nota = nota

    def CumplirAnos(self):
        self.Edad += 1


alumno = Alumno()