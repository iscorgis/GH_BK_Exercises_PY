# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#solución profesor
def semaforo(estado_sema):
    if estado_sema == "verde":
        print("puede cruzar la calle")
    else:
        print("esperar")

#solución alumno
def switch_semaforo(color):
    switcher = {
        "verde":    "pude pasar",
        "amarillo": "esperar",
        "rojo":     "no puede pasar",

    }
    print( switcher.get(color,"Valor introducido no se corresponde con los colores disponibles: Verde, amarillo, rojo") )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Introduce el color del semaforo")
    #switch_semaforo(input() )

    semaforo("verde")
