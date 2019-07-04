"""
Ejercicio 2
Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe
que ese numero está entre los dos (dentro del rango).
"""


def range_number(number, start, end):
    user_number = int(input(number))
    result = ""

    if user_number in range(start, end):
        result = "True"
    elif user_number not in range(start, end):
        result = "False"

    return result


print(range_number("Dime tu numero: ", 1, 101))
