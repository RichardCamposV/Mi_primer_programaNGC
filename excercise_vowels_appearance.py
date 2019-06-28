"""
Ejercicio 3
Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string "aurora boreal"
se convertira en "12r3r4 b5r67l"
"""
vowels = ["a", "e", "i", "o", "u"]
n_vowels = 0

user_string = input("Escribe tu frase: ")

for value in user_string:
    if value in vowels:
        n_vowels += 1
        user_string = user_string.replace(value, str(n_vowels), 1)

print(user_string)
