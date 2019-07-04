
def input_with_confirmation(question):
    confirmation = False

    while not confirmation:
        data_user = input(question)
        sure = input("Has dicho {}, ¿Estás seguro? [Si / No]: ".format(data_user)).upper()
        if sure == "SI":
            confirmation = True
    return data_user


name = input_with_confirmation("¿Como te llamas?: ")
print("Has confirmado que te llamas {}".format(name))

number = input_with_confirmation("Dime un numero: ")
print("Has confirmado que tu numero es {}".format(number))