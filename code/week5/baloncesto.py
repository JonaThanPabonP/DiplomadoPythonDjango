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
    opc = int(input("Ingrese la opción necesaria: "))
    
    if opc == 0:
        flag = False

    elif opc == 1:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
    
    elif opc == 2:
        fecha = input("Fecha: ")
        ubicacion = input("Lugar: ")
        
    elif opc == 3:
        id_jugador = input("ID del jugador: ")
        id_partido = input("ID del partido: ")
        puntos_partido = input("Puntos partido: ")
        faltas_partido = input("Faltas partido: ")


class Jugador:
    """
    this class jugador
    """
    def __init__(self, id, name, age) -> None:
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
    def __init__(self, id, date, location) -> None:
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