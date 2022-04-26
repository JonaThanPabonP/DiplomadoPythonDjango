# Un equipo de baloncesto local tiene la intención de determinar quiénes son sus mejores jugadores

# Los jugadores pueden tener datos como nombre, edad, partidos jugados, y numero de anotación totales,
# Hacer un programa que permita ingresar dichos valores y al final muestre los resultados de quien tiene un mejor promedio de anotaciones

jugadores = []
mejor_jug = {"nombre":"", "anotaciones":0}

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

# print(jugadores)
for jugador in jugadores:
    if jugador["anotaciones"] > mejor_jug["anotaciones"]:
        mejor_jug.update({"nombre":jugador["nombre"], "anotaciones":jugador["anotaciones"]})

print(mejor_jug)