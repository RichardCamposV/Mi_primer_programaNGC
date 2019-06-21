
operation_number1 = 0
operation_number2 = 0
result = 0

print("CALCULADORA")
print("(Suma(1) / Resta(2) / Multiplicacion(3) / Division(4))")
user_operation = int(input("¿Qué operación desea realizar?: "))

while user_operation > 0:

    if user_operation == 1:
        operation_number1 = int(input('\n'"Primer numero: "))
        operation_number2 = int(input("Segundo numero: "))
        result = operation_number1 + operation_number2

    elif user_operation == 2:
        operation_number1 = int(input('\n'"Primer numero: "))
        operation_number2 = int(input("Segundo numero: "))
        result = operation_number1 - operation_number2

    elif user_operation == 3:
        operation_number1 = int(input('\n'"Primer numero: "))
        operation_number2 = int(input("Segundo numero: "))
        result = operation_number1 * operation_number2

    elif user_operation == 4:
        operation_number1 = float(input('\n'"Primer numero: "))
        operation_number2 = float(input("Segundo numero: "))
        result = operation_number1 / operation_number2

    print('\n'"El resultado de su operacion es: {} ".format(result))

    user_operation = int(input("Desea hacer otra operacion (Si (1) / No (0)): "))

    if user_operation == 1:
        print('\n'"(Suma(1) / Resta(2) / Multiplicacion(3) / Division(4))")
        user_operation = int(input("¿Qué operación desea realizar?: "))

print('\n'"Gracias por usar nuestra calculadora")
