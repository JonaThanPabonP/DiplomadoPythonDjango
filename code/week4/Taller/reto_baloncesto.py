class Player:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Game:
    def __init__(self, date, location):
        self.date = date
        self.location = location

class GamePlayed:
    def __init__(self, game, player, points, faults):
        self.game = game
        self.player = player
        self.points = points
        self.faults = faults
    def anotaciones(self, new_point):
        pass


player1 = Player(id="J1",name="Yurley",age=13)
player2 = Player(id="J2",name="Maria",age=18)
player3 = Player(id="J3",name="Yurley",age=15)
player4 = Player(id="J4",name="Yurley",age=13)
player5 = Player(id="J5",name="Yurley",age=13)
player6 = Player(id="J6",name="Yurley",age=13)
player7 = Player(id="J7",name="Yurley",age=13)
player8 = Player(id="J8",name="Yurley",age=13)
player9 = Player(id="J9",name="Yurley",age=13)
player10 = Player(id="J10",name="Yurley",age=13)

list_players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]

for player in list_players:
    if player.age >= 15:
        print(player.name, player.age)