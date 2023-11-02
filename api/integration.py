from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name)

CORS(app)

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

@app.route('/get_random_player', methods=["GET"])
def get_random_player():
    random_player, _ = random.choices(players, weights=weights)[0]
    player_info = {
        "Name": random_player.name,
        "Position": random_player.pos,  # Removed extra space
        "Overall": random_player.ovr,  # Removed extra space
        "Pace": random_player.pac,  # Removed extra space
        "Shooting": random_player.sho,  # Removed extra space
        "Passing": random_player.pas,  # Removed extra space
        "Dribbling": random_player.dri,  # Removed extra space
        "Defense": random_player.defe,  # Removed extra space
        "Physicality": random_player.phy
    }
    return jsonify(player_info)

if __name__ == '__main__':
    app.run(host='localhost', port=8281)
