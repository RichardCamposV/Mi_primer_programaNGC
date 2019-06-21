
number_guess = 0
user_number = 0

print("Escribe un numero del 1 al 12 tu compnero tratara de adivinarlo")
number_guess = int(input("Numero: "))

print('\n'"Adivina el numero")
user_number = int(input("Numero: "))

if number_guess == user_number:
    print("¡Felicidades has adivinado!")

else:
    while number_guess is not user_number:
        user_number = int(input("Intenta de nuevo: "))

        if number_guess == user_number:
            print("¡Felicidades has adivinado!")

            




