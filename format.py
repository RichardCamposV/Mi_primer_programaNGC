"""
Programa un codigo que utilizando el metodo replace de las strings se sustituya las claves de mi string inicial
por los valores en orden de una lista
"""
value_to_change = [1, 2, "hola", "adios"]
string_to_change = "Hola, el numero {}, numero {}, {} y {}"

for valor in value_to_change:
    string_to_change = string_to_change.replace("{}", str(valor), 1)

print(string_to_change)