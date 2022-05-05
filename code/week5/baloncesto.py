def menu():
    print("1. Ingresar nuevo jugador.")
    print("2. Ingresar nuevo partido.")
    print("3. Ingresar datos de jugador en juego.")
    print("4. Mostrar resultados.")
    print("5. Mostrar todos los jugadores.")
    print("0. Salir.")


flag = True
while flag:
    menu()
    opc = input("Ingrese la opción necesaria: ")
    
    if opc == 0:
        flag = False

    elif opc == 1:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        