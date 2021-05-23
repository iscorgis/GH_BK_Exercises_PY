

lista_nombres = []

def add_nombres_tolista(nombre):
    lista_nombres.append(nombre)

salida_while = False

while not salida_while:
    print("Quiere introducir un nombre en la lista?")
    if input() == 'True':
        print("Introduzca el nombre:")
        add_nombres_tolista(input())
    else:
        salida_while = True

for i in lista_nombres:
    print(i)
