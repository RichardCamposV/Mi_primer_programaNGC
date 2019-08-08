"""
Ejercicio 3
Crea un programa que pregunte al usuario que adivine un numero del 1 al 10, pero ese numero se va
a generar aleatoriamente. Hacer esperar al usuario 3 segundos antes de dar la respuesta.
"""
from time import sleep
import random

COUNT_TIME = 3
LIFES_GAME = 3


def number_to_guess(number):
    correct_number = False
    trys = 0
    guees_number = int(random.random() * 10)

    while not correct_number:
        print("¡Adivina el numero!")
        print("Numero del 1 al 10")
        user_number = int(input(number))
        if guees_number == user_number:
            sleep(COUNT_TIME)
            print("¡¡Felicidades!!, adivinaste")
            correct_number = True
        else:
            sleep(COUNT_TIME)
            print("Incorrecto, intenta de nuevo\n")
            trys += 1
            if trys == LIFES_GAME:
                print("¡¡Lo siento!!, perdidste")
                correct_number = True


print(number_to_guess("Dime tu numero: "))
