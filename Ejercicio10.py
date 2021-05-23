
#Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número
#buscado. También poner el número de intentos requeridos.

from random import seed
from random import randint
seed(1)
number_answer = randint(0,20)

while True:
    number = input("Insert your number ")
    try:
        number = float(number)

        if number < number_answer:
            print("Your number is smaller ")
        elif number > number_answer:
            print("Your number is bigger")
        else:
            print("It's your number!!")
            break
    except ValueError:
        print("The input is not correct, please, try again:")