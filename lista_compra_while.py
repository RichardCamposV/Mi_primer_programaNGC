
mi_lista = []
input_user = ""

input_user = input("¿Que deseas comprar? (Escribe FIN para salir): "'\n').upper()

while input_user != "FIN":
    mi_lista.append(input_user)
    input_user = input("¿Que deseas comprar? (Escribe FIN para salir): "'\n').upper()

"""
 Este codigo es lo mismo que el for

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:

    #item = mi_lista[indice_actual]
    
Lo de arriba es lo mismo que esta escrito en el .format()
Nada mas sustituimos item en el format = .format(item)
El indice_actual extrae cada uno de los productos que estan en la lista

    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1
"""

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("Esta es la lista de las compras")
