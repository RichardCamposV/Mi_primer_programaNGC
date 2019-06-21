
number_user = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(10, 0, -1):
    print("{} x {} = {}".format(number_user, multiplo, number_user * multiplo))

