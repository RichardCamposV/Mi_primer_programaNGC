
text_user = input("Escribe tu frase: ")

result = []
vowels = ["a", "e", "i", "o", "u"]

for letra in text_user:

    if letra in vowels:
        result.append(letra)

print("Vocales = {}".format(result))
