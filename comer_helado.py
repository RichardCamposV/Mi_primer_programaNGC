
apetece_helado_input = input("¿Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te dije que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ").upper()
senor_helados_input = input("¿Esta el senor de los helados? (Si / No): ").upper()
tia_input = input("¿Esta tu tia? (Si / No): ")

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or tia_input == "SI"
senor_helados = senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and senor_helados:
    print("Pues comete un helado")

else:
    print("Pues nada")
