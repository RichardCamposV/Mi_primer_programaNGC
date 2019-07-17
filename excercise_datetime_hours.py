"""
Ejercicio 3
Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento
"""
import datetime

day = int(input("Dime el dia: "))
month = int(input("Dime el mes: "))
year = int(input("Dime el año: "))

user_date = datetime.datetime(year=year, month=month, day=day)
time_remaining = datetime.datetime.now() - user_date

print("Han pasado {} horas".format(int(time_remaining.total_seconds()/3600)))
