"""
Ejercicio 3
Cre un programa que sea capaz de contar la cantidad de letras mayusculas en una string introducida por el usuario
"""
text_user = input("Escribe tu frase: ")

vowels = ["A", "E", "I", "O", "U"]
consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
n_capletter = 0

# Al  usar el .uppercase() me cuenta tambien los simbolos y los espacios entre cada palabra

for letra in text_user:

    if letra in vowels:
        n_capletter += 1
    elif letra in consonants:
        n_capletter += 1

print("Mayusculas = {}".format(n_capletter))

