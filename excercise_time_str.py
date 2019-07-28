"""
Ejercicio 1
Escribe una frase aleatoria de una lista de strings cada 3 segundos
"""
from time import sleep
import random

label_strings = ["hi", "games", "food", "F** U", "What?", "Again"]
TIME_STRING = 3
START_STRING = 0
END_STRING = 5
counter_strings = 0

while True:
    sleep(TIME_STRING)
    counter_strings = random.randint(START_STRING, END_STRING)
    print(label_strings[counter_strings])
