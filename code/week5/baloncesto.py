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
        


class Jugador:
    """
    this class jugador
    """
    def __init__(self, id, name, age) -> None:
        self.id = id
        self.name = name
        self.age = age


class Partido:
    """
    this class partido
    """
    def __init__(self, id, date, location) -> None:
        self.id = id
        self.date = date
        self.location = location


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