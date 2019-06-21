
"""
Crea un programa que te cuente el numero de vocales y consonantes dentro de una frase introducida por el usuario
"""

frase_del_usuario = input("Escribe tu frase: ")

vocales = ["a", "e", "i", "o", "u"]

n_vocales = 0
n_consonantes = 0

for letra in frase_del_usuario:

    if letra in vocales:
        n_vocales += 1

    else:
        n_consonantes += 1

print("Las vocales son {}".format(n_vocales))
print("Las consonantes son {}".format(n_consonantes))
