"""
Ejercicio 1
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimientos
"""

schedule_friends = dict()
confirmation = False

while not confirmation:
    print("¿Que quieres hacer?")
    action = input("Añadir un nuevo amigo [1] / Consultar fecha [2] / Salir [S]: ").upper()

    if action == "1":
        name = input("Ingresa el nombre: ")
        date = input("Ingresa la fecha de nacimiento (dd/mm/aaaa): ")
        schedule_friends[name] = date

    elif action == "2":
        name = input("¿De quien quieres checar su edad?: ")
        print(schedule_friends[name])

    elif action == "S":
        confirmation = True

