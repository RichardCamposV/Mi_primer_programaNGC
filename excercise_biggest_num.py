"""
Ejercicio 2
Crear un programa que encuentre el numero más grande de una lista
(sin usar la funcion max())
"""

numbers = [1, 2, 3, 8, 9, 12, 3, 4, 17, 20, 10]
biggest_number = numbers[0]

for value in numbers:

    if value > biggest_number:
        biggest_number = value

print("El numero mas grande es: {}".format(biggest_number))
