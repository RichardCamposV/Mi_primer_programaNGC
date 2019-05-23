

number_to_guess = 2

print("Adivina el numero del 1 al 10")
print("Tienes 5 intentos")

user_number = int(input("Adivina el numero: "))

if number_to_guess == user_number:
    print("¡Felicidades has adivinado el numero!")
else:
    user_number = int(input("Intenta de nuevo: "))

    if number_to_guess == user_number:
        print("¡Felicidades has adivinado el numero!")
    else:
        user_number = int(input("Intenta de nuevo: "))

        if number_to_guess == user_number:
            print("¡Felicidades has adivinado el numero!")
        else:
            user_number = int(input("Intenta de nuevo: "))

            if number_to_guess == user_number:
                print("¡Felicidades has adivinado el numero!")
            else:
                user_number = int(input("Intenta de nuevo: "))

                if number_to_guess == user_number:
                    print("¡Felicidades has adivinado el numero!")
                else:
                    print("Lo siento, perdiste")
