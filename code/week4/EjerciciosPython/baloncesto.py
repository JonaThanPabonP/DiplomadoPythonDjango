# Un equipo de baloncesto local tiene la intención de determinar quiénes son sus mejores jugadores

# Los jugadores pueden tener datos como nombre, edad, partidos jugados, y numero de anotación totales,
# Hacer un programa que permita ingresar dichos valores y al final muestre los resultados de quien tiene un mejor promedio de anotaciones

jugadores = []
mejor_jug = {"nombre":"", "promedio":0}
bandera = True

while bandera == True:
    # Menu
    print("-------------------------------------")
    print("-------          Menu         -------")
    print("-------------------------------------")
    print("1. Registrar jugadores.")
    print("2. Ver jugador con mejor promedio de anotaciones.")
    print("3. Listar jugadores.")
    print("0. Salir.")
    opc = int(input("Ingrese la opción escogida: "))


    if opc == 1:
        # Registrar jugadores
        cant_jug = int(input("Ingrese la cantidad de jugadores a registrar: "))
        while cant_jug>0:
            jugador = {}
            cant_jug -= 1
            nombre = input("Ingrese el nombre del jugador: ")
            edad = int(input("Ingrese la edad del jugador: "))
            partidos = int(input("Ingrese el numero de partidos jugados del jugador: "))
            anotaciones = int(input("Ingrese el total de anotaciones totales del jugador: "))

            jugador.update({"nombre":nombre, "edad":edad, "partidos": partidos, "anotaciones": anotaciones}
            )
            jugadores.append(jugador)
   
    elif opc == 2:
        # Mostrar jugador mejor promedio
        for jugador in jugadores:
            if (jugador["anotaciones"]/jugador["partidos"]) > mejor_jug["promedio"]:
                mejor_jug.update({"nombre":jugador["nombre"], "promedio":(jugador["anotaciones"]/jugador["partidos"])})
        print(mejor_jug)
    
    elif opc == 3:
        # Listar jugadores
        print(jugador for jugador in jugadores)

    elif opc == 0:
        bandera = False
        print("Saliendo...")