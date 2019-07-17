"""
Ejercicio 4
Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como
larga sea la string.
"""


def bars_strings(sentences):
    symbol = ""
    for data in sentences:
        symbol += data.replace(data, "-")
    return symbol


print(bars_strings("Hola mundo"))
print(bars_strings("Como estas amigo?"))
