from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
CORS(app)
api = Api(app)

# Define position values
CF = "Center Forward"
ST = "Striker"
RB = "Right Back"
LB = "Left Back"
CM = "Central Midfield"
LW = "Left Wing"
CDM = "Central Defensive Midfield"
CB = "Center Back"
RM = "Right Midfield"
LM = "Left Midfield"
LD = "Left Back"
CAM = "Central Attacking Midfield"
RW = "Right Wing"
LWB = "Left Wing Back"
RWB = "Right Wing Back"

class Player:
    def __init__(self, name, pos, ovr, pac, sho, pas, dri, defe, phy):
        self.name = name
        self.pos = pos
        self.ovr = ovr
        self.pac = pac
        self.sho = sho
        self.pas = pas
        self.dri = dri
        self.defe = defe
        self.phy = phy

players = [
    (Player("Lionel Messi", CF, 90, 80, 87, 90, 94, 33, 64), 1 / 100),
    (Player("Cristiano Ronaldo", ST, 86, 85, 90, 75, 92, 45, 78), 1 / 86),
    # Add more player data here...
]

weights = [1 if player.ovr <= 70 else 0.5 for player, _ in players]

class RandomPlayer(Resource):
    def get(self):
        random_player, _ = random.choices(players, weights=weights)[0]
        player_info = {
            "Name": random_player.name,
            "Position": random_player.pos,
            "Overall": random_player.ovr,
            "Pace": random_player.pac,
            "Shooting": random_player.sho,
            "Passing": random_player.pas,
            "Dribbling": random_player.dri,
            "Defense": random_player.defe,
            "Physicality": random_player.phy
        }
        return player_info

api.add_resource(RandomPlayer, '/get_random_player')

if __name__ == '__main__':
    app.run(host='localhost', port=8281)
