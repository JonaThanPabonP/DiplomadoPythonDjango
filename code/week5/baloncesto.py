

def menu():
    print("--- MENU ---")
    print("1. Ingresar nuevo jugador.")
    print("2. Ingresar nuevo partido.")
    print("3. Ingresar datos de jugador en juego.")
    print("4. Mostrar resultados.")
    print("5. Mostrar todos los jugadores.")
    print("0. Salir.")


class Jugador:
    """
    this class jugador
    """
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def get_player_by_id(id):
        player = None
        return player

class Partido:
    """
    this class partido
    """
    def __init__(self, id, date, location):
        self.id = id
        self.date = date
        self.location = location

    def get_game_by_id(id):
        game = None
        return game

class JugadorPartido:
    """
    this class jugador en partido
    """
    def __init__(self, player, game, points, faults):
        self.game = game
        self.player = player
        self.points = points
        self.faults = faults

    def anotaciones(self, new_points):
        self.points += new_points

    def faltas(self, new_faults):
        self.faults += new_faults

    def get_points_by_game(points):
        points_by_game = None
        return points_by_game


jugadores = []
partidos = []
infopartidos = []

def inicio():
    flag = True
    while flag:
        menu()
        opc = int(input("Ingrese la opción necesaria: "))
        
        if opc == 0:
            print("Hasta luego!")
            flag = False

        elif opc == 1:
            id_jug = input("ID: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            jug = Jugador(id_jug,nombre,edad)
            jugadores.append({"id": jug.id, "nombre": jug.name, "edad": jug.age})
        
        elif opc == 2:
            id_part = input("ID partido: ")
            fecha = input("Fecha: ")
            ubicacion = input("Lugar: ")
            part = Partido(id_part,fecha,ubicacion)
            partidos.append({"id": part.id, "fecha": part.date, "ubicacion": part.location})
            
        elif opc == 3:
            id_jugador = input("ID del jugador: ")
            id_partido = input("ID del partido: ")
            puntos_partido = input("Puntos partido: ")
            faltas_partido = input("Faltas partido: ")
            jugpart = JugadorPartido(id_jugador, id_partido, puntos_partido, faltas_partido)
            
            infopartidos.append({"id_jug": jugpart.player, "id_part":jugpart.game, "puntos":jugpart.points, "faltas":jugpart.faults})

            
           
        elif opc == 4:
            if infopartidos == []:
                print("No hay registros.")
            else: 
                for jug in infopartidos:
                    print(jug)


        elif opc == 5:
            if jugadores == []:
                print("No hay registros.")
            else:
                for jugador in jugadores:
                    print(jugador)

inicio()