"""
Crea un programa que cambie todas las 'A' o 'a' por la string "VACA" de una string introducida por el usuario
"""
total = ""

user_string = input("Escribe alguna palabra: ").upper()

for value in user_string:
    total = user_string.replace("A", "VACA")

print(total)