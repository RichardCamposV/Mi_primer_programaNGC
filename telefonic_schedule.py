
schedule = dict()
exit_schedule = False

while not exit_schedule:
    action = input("¿Que quieres hacer? [Añadir numero[A] / Consultar numero[C] / Salir [S]]: ").upper()

    # Acción añadir
    if action == "A":
        print("Vamos a añadir un número de telefono: ")
        print("---------------------------------------")
        name = input("Nombre: ")
        number = input("Número: ")
        schedule[name] = number

    # Acción consultar
    elif action == "C":
        print("Consultar numero: ")
        print("---------------------------------------")
        name = input("De quien quieres saber el numero: ")
        print(schedule[name])

    # Acción salir
    elif action == "S":
        exit_schedule = True