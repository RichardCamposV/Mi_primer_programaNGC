"""
Pregunta al usuario una serie de 10 numeros, determina cual es el mas grande de los 10
"""

user_numbers = []
number_ofthe_user = ""

while len(user_numbers) < 10:
    while not number_ofthe_user.isdigit():
        number_ofthe_user = input("Dime tu numero: ")
    user_numbers.append(int(number_ofthe_user))
    number_ofthe_user = ""
    print("¡Numero añadido!")

biggest_number = user_numbers[0]

for number in user_numbers:
    if number > biggest_number:
        biggest_number = number

print('\n'"El numero mas grande es {}".format(biggest_number))
