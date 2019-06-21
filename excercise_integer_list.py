"""
Dada una lista de numeros, devolver el resultado de la multiplicacion de todos los numeros
"""

integer_list = [12, 9, 20, 7, 2, 4, 1]
total = 1

for number in integer_list:
    total *= number

print(total)
