"""
Ejercicio 3
Dada una lista mixta de enteros y strings, devolver dos listas una con todos los enteros y otra con todas las strings
"""
mix_list = [2, "hola", 12, "comida", 3, 4, 65, "hemoshi", "games", 9]
integer = []
strings = []

for data in mix_list:
    data = str(data)

    if data.isdigit():
        integer.append(data)
    else:
        strings.append(data)

print("Lista de los enteros: {} \nLista de las strings: {} ".format(integer, strings))