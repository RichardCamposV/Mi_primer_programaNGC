"""
Ejercicio 2
Escribe un programa que imprima por pantalla una frase aleatoria cada segundo. La lista de frases
de la que se seleccionará la frase aleatoria será distinta según el segundo en el que estemos.
"""
from time import sleep
import random

COUNT_TIME = 1
current_time = 0

base_phrases = ["Frases ", "Nombres de ", "Sonidos de "]
phrases = ["alegres", "odio", "absurdas", "motivacionales", "tristes"]
names = ["muebles(silla, mesa)", "bebidas", "comidas", "animales"]


def random_strings(text_list, label_phrases, label_names):
    final_position = int(random.random() * len(text_list))

    if final_position != 0:
        text = int(random.random() * len(label_phrases))
        print(text_list[final_position] + label_phrases[text])
    else:
        text = int(random.random() * len(label_names))
        print(text_list[final_position] + label_names[text])


while True:
    sleep(COUNT_TIME)
    print("-Segundos acabados en {}: ".format(current_time))
    random_strings(base_phrases, names, phrases)
    current_time += 1
