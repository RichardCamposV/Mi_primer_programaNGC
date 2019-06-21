"""
Dada una lista de strings, devolver una lista con el largo de cada string
"""

string_list = ["asdki", "atun", "camote", "forever", "control"]
range_list = []

for number in string_list:
    total = len(number)
    range_list.append(total)

print(range_list)