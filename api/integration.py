from flask import Flask, jsonify
import random

app = Flask(__name__)

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
    (Player("Erling Haaland", ST, 91, 89, 93, 66, 80, 24, 88), 1 / 91),
    (Player("Kylian Mbappe", ST, 91, 97, 90, 80, 92, 36, 78), 1 / 91),
    (Player("Sergi Roberto", RB, 80, 74, 63, 79, 77, 75, 73), 1 / 40),
    (Player("Ryota Morioka", CM, 72, 42, 69, 74, 69, 71, 68), 1 / 40),
    (Player("Kevin De Bruyne", CM, 91, 72, 88, 94, 87, 65, 78), 1 / 91),
    (Player("Neymar Jr", LW, 89, 86, 83, 85, 93, 37, 61), 1 / 89),
    (Player("Sandro Tonali", CDM, 86, 84, 74, 81, 81, 82, 84), 1 / 70),
    (Player("Qiu Zhongyi", CB, 48, 56, 25, 27, 34, 51, 52), 1 / 35),
    (Player("Marcus Rashford", LW, 85, 90, 86, 78, 84, 42, 74), 1 / 85),
    (Player("Vinicius Jr", LW, 89, 95, 82, 78, 90, 29, 68), 1 / 89),
    (Player("Bruno Fernandes", CAM, 88, 71, 86, 90, 83, 69, 77), 1 / 88),
    (Player("Heung Min Son", LW, 87, 87, 88, 80, 84, 42, 70), 1 / 88),
    (Player("Kaoru Mitoma", LM, 80, 84, 73, 74, 85, 57, 65), 1 / 45),
    (Player("Eberechi Eze", CAM, 79, 77, 76, 77, 82, 49, 68), 1 / 50),
    (Player("Chris Donnell", CM, 55, 63, 47, 52, 56, 48, 65), 1 / 35),
    (Player("Son Seung Woo", RWB, 48, 62, 26, 34, 44, 47, 51), 1 / 40),
    (Player("Jayden Harris", CDM, 58, 66, 48, 53, 54, 54, 69), 1 / 70),
    (Player("James Madisson", CAM, 84, 71, 81, 86, 86, 54, 63), 1 / 67),
    (Player("James Gibbons", RB, 62, 71, 43, 57, 62, 58, 64), 1 / 35),
    (Player("Paulo Dybala", CF, 86, 80, 85, 85, 90, 40, 60), 1 / 82),
    (Player("Hakan Calhanoglu", CM, 85, 67, 80, 86, 85, 70, 66), 1 / 70),
    (Player("Iago Aspas", ST, 85, 81, 85, 79, 86, 35, 64), 1 / 70),
    (Player("Antony", RM, 70, 83, 58, 63, 73, 38, 51), 1 / 50),
    (Player("Vakoun Issouf Bayo", ST, 70, 76, 70, 54, 67, 25, 77), 1 / 40),
    (Player("Noah Katterbach", LB, 69, 71, 40, 57, 72, 66, 58), 1 / 42),
    (Player("Paul Lasne", CDM, 69, 43, 61, 70, 67, 66, 70), 1 / 42),
    (Player("Auli Oliveros", CAM, 69, 81, 66, 66, 71, 59, 63), 1 / 42),
]

weights = [1 if player.ovr <= 70 else 0.5 for player, _ in players]

@app.route('/get_random_player', methods=['GET'])
def get_random_player():
    random_player, _ = random.choices(players, weights=weights)[0]
    player_info = {
        "Name": random_player.name,
        "Position ": random_player.pos,
        "Overall ": random_player.ovr,
        "Pace ": random_player.pac,
        "Shooting ": random_player.sho,
        "Passing ": random_player.pas,
        "Dribbling ": random_player.dri,
        "Defense ": random_player.defe,
        "Physicality": random_player.phy
    }
    return jsonify(player_info)

if __name__ == '__main__':
    app.run()
