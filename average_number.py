
list_user = []
number_user = ""
large_list = 0
total = 0

while number_user != "Fin":
    print("Escribe Fin para terminar")
    number_user = input("Dime tu numero: ")
    if number_user.isdigit():
        list_user.append(int(number_user))
        print("¡Numero añadido!")

for number in list_user:
    total += number
    large_list += 1

print("Media = {}".format(total / large_list))
