"""
Ejercicio 1
Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5,
cambiar el texto por "Bazinga"
"""

numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 20, 15, 30, 60, 70]

for index in range(len(numbers)):
    number = numbers[index]

    if number % 3 == 0 or number % 5 == 0:
        numbers[index] = ""
        if number % 3 == 0:
            numbers[index] += "Fizz"
        elif number % 5 == 0:
            numbers[index] += "Buzz"
        if number % 3 == 0 and number % 5 == 0:
            numbers[index] = "Bazinga"

print(numbers)