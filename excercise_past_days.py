"""
Ejercicio 1
Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana
"""

import datetime

weekdays = {0: "Lunes",
            1: "Martes",
            2: "Miercoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sabado",
            6: "Domingo"}

past = datetime.datetime.now() + datetime.timedelta(days=-5)
day_past = past.weekday()

print("Hace 5 dias respecto hoy fue {}".format(past.strftime("%d del %m de %Y")))

if day_past in weekdays:
    print("Ese dia fue {}".format(weekdays[day_past]))

