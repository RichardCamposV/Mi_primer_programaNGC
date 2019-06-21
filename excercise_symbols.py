
text_user = input("Escribe tu frase: ")

spaces = [" "]
symbols = [".", ","]

n_spaces = 0
n_commas = 0
n_points = 0

for letra in text_user:

    if letra in spaces:
        n_spaces += 1

    elif letra in symbols:

        if letra == ".":
            n_points += 1
        elif letra == ",":
            n_commas += 1

print("Espacios son: {}".format(n_spaces))
print("Comas son: {}".format(n_commas))
print("Puntos son: {}".format(n_points))
