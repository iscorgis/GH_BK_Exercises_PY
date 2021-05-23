# Programa to calculate the user IMC

def read_kilos():
    while True:
        weight_kg = input("Insert your weight in KG: ")
        try:
            weight_kg = float(weight_kg)
            return weight_kg
        except ValueError:
            print("The input is not correct, please, Insert your weight in KG:")

def read_height():
    while True:
        height_m = input("Insert your height in meters")
        try:
            height_m = float(height_m)
            return height_m
        except ValueError:
            print("The input is not correct, please, Insert your height in meters:")

def imc_calculation(height,weight):
    try:
        imc = weight / (pow(height, 2))
        return imc
    except ValueError:
        print("The input values are not valid")

no_exit = True
while no_exit:
    weight_kg = read_kilos()
    height_m = read_height()
    print("Your IMC is: {0}".format( imc_calculation(height_m,weight_kg) ) )

    if input('Desea Continuar Si(1)/No(2)') != 1 :
       no_exit = False
