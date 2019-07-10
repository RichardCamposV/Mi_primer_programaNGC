"""
Ejercicio 2
Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés.
"""

colors_category = {"rojo": "red",
                   "azul": "blue",
                   "amarillo": "yellow",
                   "negro": "black",
                   "naranja": "orange",
                   "cafe": "brown",
                   "verde": "green",
                   "gris": "gray",
                   "morado": "purple",
                   "blanco": "white"}
confirmation = False

while not confirmation:
    print("Para salir [S]")
    user_color = input("Color: ")

    if user_color != "S":
        print(colors_category[user_color])

    else:
        confirmation = True
