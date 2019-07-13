"""
Ejercicio 3
Crea un programa que cuente el número de veces que aparece una plabra en una string
"""

form_strings = dict()
word = ""
number_string = 1

user_string = input("Escribe tu frase: ")

for data in user_string:
    word += data
    length = len(word) - 1
    if word in form_strings:
        form_strings[word] += 1
        word = ""
    elif data == " ":
        if length != 0:
            form_strings[word.replace(" ", "")] = number_string
        word = ""

print(form_strings)
