
health_pikachu = 100
health_enemy = 0
atack_pokemon = 0
name_pokemon = str

print("Pokemon enemigo: (1)Bulbasaur, (2)Charmander, (3)Squirtl")
user_enemy = int(input("Eliga con que pokemon quiere pelear: "))

# Condiciones sobre que enemigo vamos a elegir y sus caracteristicas
if user_enemy == 1:
    health_enemy = 100
    name_pokemon = "Bulbasaur"
    atack_pokemon = 10

elif user_enemy == 2:
    health_enemy = 80
    name_pokemon = "Charmander"
    atack_pokemon = 7

elif user_enemy == 3:
    health_enemy = 90
    name_pokemon = "Squirtl"
    atack_pokemon = 8

while health_pikachu > 0 and health_enemy > 0:
    print("Tu oponente sera {}"'\n'.format(name_pokemon))
    print("Pikachu vs {}".format(name_pokemon))
    print("¡Que empiece la pelea!")

    # Elegimos el ataque
    print('\n'"(1)Ataque chispazo, (2) Ataque bola voltio")
    user_select_damage = int(input("Ataque a realizar (1 / 2): "))

    if user_select_damage == 1:
        health_enemy -= 10
        print("Pikachu hizo un ataqque de 10 de daño")
    elif user_select_damage == 2:
        health_enemy -= 12
        print("Pikachu hizo un ataqque de 12 de daño")

    # Impresion de valores finales tanto del enemigo como aliado
    print("La vida de {} es de: {}".format(name_pokemon, health_enemy))

    print("{} te hizo un ataque de {} de daño".format(name_pokemon, atack_pokemon))

    health_pikachu -= atack_pokemon
    print("La vida de Pikachu: {}".format(health_pikachu))

if health_pikachu <= 0:
    print('\n'"¡Pikachu a perdido!")
if health_enemy <= 0:
    print('\n'"¡Pikachu a ganado!")

print("El combate ha terminado")
