"""
Obtener los tipos de datos que hay en una lista
"""

data_list = [1, 2, 3, "asd", False, [], True, 23, 2.1]
types_list = []

for data in data_list:
    types_list.append(type(data))

print(types_list)