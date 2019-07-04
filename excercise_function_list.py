"""
Ejercicio 3
Escribe una función que reciba una lista de números y devuelva
otra pero conteniendo solo los números pares.
"""


def pairs_list(numbers):
    list_number = []
    pairs = []
    confirmation = False

    while not confirmation:
        user_number = input(numbers)
        if user_number.isdigit():
            list_number.append(int(user_number))
            sure = input("¿Deseas agregar otro número? [Si / No]: ").upper()
            if sure != "SI":
                confirmation = True

    for data in list_number:
        if data % 2 == 0:
            pairs.append(data)

    return pairs


print(pairs_list("Dime tu numero: "))
