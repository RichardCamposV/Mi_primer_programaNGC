"""
Ejercicio 1
Escribe una función que encuentre el numero más grande entre 3 numeros
"""


def max_number(numbers):
    list_number = []
    confirmation = False
    while not confirmation:
        user_number = input(numbers)
        if user_number.isdigit():
            list_number.append(int(user_number))
            sure = input("¿Quieres seguir agregando numeros? [Si / No]: ").upper()
            if sure != "SI":
                confirmation = True
    list_number = max(list_number)

    return list_number


print(max_number("Dime tu numero: "))

