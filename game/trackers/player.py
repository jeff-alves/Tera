
class Player(object):

    def __init__(self):
        pass

    def pos(self, pos1, pos2, angle, speed, typ, time):
        self.pos1 = pos1
        self.pos2 = pos2
        self.angle = angle
        self.speed = speed
        self.typ = typ
        self.time = time

        print("Event (Player_pos): ", self.pos2, self.angle, self.speed, self.typ, self.time)

    def login(self, name, race, gender, classe, id, server_id, player_id):
        self.name = name
        self.race = race
        self.gender = gender
        self.classe = classe
        self.id = id
        self.server_id = server_id
        self.player_id = player_id

        print("Event (Player_login): ", name, race, gender, classe, player_id, id)
