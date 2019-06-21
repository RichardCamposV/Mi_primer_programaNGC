
"""
Obtener la tabla de multiplicar de un numero especificado por el usuario
"""

number_chart = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(1, 11):

    if multiplo % 2 == 0:
        print("{} x {} = {}".format(number_chart, multiplo, number_chart * multiplo))
