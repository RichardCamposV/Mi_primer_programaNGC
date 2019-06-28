"""
Ejercicio 2
Crear un programa que le repita al usuario todo lo que dice pero con todas la vocales cambiadas por 'i'
"""
vowels = ["a", "e", "i", "o", "u"]

user_sentences = input("Escribe alguna frase: ")

for value in user_sentences:
    if value in vowels:
        user_sentences = user_sentences.replace(value, "i", 1)

print(user_sentences)
