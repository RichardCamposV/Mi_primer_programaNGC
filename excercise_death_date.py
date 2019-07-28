"""
Falta implementar la opcion "A veces" que es la mitad de cada penalización
"""
import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 6
DRINKER_PENALIZATION = 6
SEDENTARY_PENALIZATION = 6

weekdays = {0: "Lunes",
            1: "Martes",
            2: "Miercoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sabado",
            6: "Domingo"}


def print_with_underscore(message):
    print(message)
    print(len(message) * "-")


def questions_penalization(message):
    response = None
    while response != "Y" and response != "N" and response != "S":
        response = input(message + "[Yez (Y)/ No (N)/ Sometimes (S)]: ").upper()
    return response == "Y"


print_with_underscore("¡Averigua cuanto te queda de vida!")
print("Responde esta encuesta para saber cuanto tiempo te queda de vida")

birth_date = input("Ingresa tu fecha de nacimiento [Formato dd/mm/yyyy]: ")
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

years_lost = 0

if questions_penalization("¿Fumas?"):
    years_lost += SMOKER_PENALIZATION

if questions_penalization("¿Bebes?"):
    years_lost += DRINKER_PENALIZATION

if not questions_penalization("¿Haces ejercicio?"):
    years_lost += SEDENTARY_PENALIZATION

base_lifespan = int(random.randint(AVERAGE_LIFESPAN / 2, AVERAGE_LIFESPAN) - years_lost)
deathday = birth_date + datetime.timedelta(days=base_lifespan * 365)
days_to_death = deathday - datetime.datetime.now()
missing = deathday.weekday()

print("Fecha de muerte {} te quedan {} dias para morir".format(deathday.strftime("%d/%m/%Y"), days_to_death.days))

if missing in weekdays:
    print("Ese dia sera {}".format(weekdays[missing]))

