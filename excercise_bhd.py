"""
Ejercicio 2
Crea un programa que te diga cuando falta para tu cumpleaños y que dia de la semana será
"""

import datetime

weekdays = {0: "Lunes",
            1: "Martes",
            2: "Miercoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sabado",
            6: "Domingo"}

print("Descubre cuanto falta para tu cumpleaños y en que dia caera:")
day = int(input("Dime el dia: "))
month = int(input("Dime el mes: "))
year = int(input("Dime el año: "))

user_date = datetime.datetime(year=year, month=month, day=day)
time_remaining = user_date - datetime.datetime.now()
missing = user_date.weekday()

print('\n'"Faltan {} dias y {} hora(s) para tu cumpleaños".format(time_remaining.days, int(time_remaining.seconds / 3600)))

if missing in weekdays:
    print("Ese dia sera {}".format(weekdays[missing]))

