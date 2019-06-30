"""
Dada una lista de enteros:
Vamos a sustituir los multiplos de 3 por un Fizz
y los multiplos de 5 sustituir por un Buzz
multiplos de 3 y de 5, vamos a sustituirlos por un FizzBuzz
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 20, 15, 30, 60, 70]

for index in range(len(numbers)):
    number = numbers[index]

    if number % 3 == 0 or number % 5 == 0:
        numbers[index] = ""

        if number % 3 == 0:
            numbers[index] += "Fizz"

        if number % 5 == 0:
            numbers[index] += "Buzz"

print(numbers)