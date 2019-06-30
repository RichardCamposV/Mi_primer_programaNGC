"""
Ejercicio 3
Crear un programa que guarde e imprima varias listas con todos los números que estén
dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7
"""
list_numbers = []
multiple_two = []
multiple_three = []
multiple_five = []
multiple_seven = []

print("Escriba Fin para salir")
user_list = input("Ingrese los numeros de su lista: ")

while user_list != "Fin":
    print("Escriba Fin para salir")
    user_list = input("Ingrese los numeros de su lista: ")
    if user_list.isdigit():
        list_numbers.append(user_list)

for value in list_numbers:
    value = int(value)
    if value % 2 == 0:
        multiple_two.append(value)
    if value % 3 == 0:
        multiple_three.append(value)
    if value % 5 == 0:
        multiple_five.append(value)
    if value % 7 == 0:
        multiple_seven.append(value)

print('\n'"Multiplos_de dos: {}".format(multiple_two))
print("Multiplos_de tres: {}".format(multiple_three))
print("Multiplos_de cinco: {}".format(multiple_five))
print("Multiplos_de seven: {}".format(multiple_seven))
