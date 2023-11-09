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

    # ... (same as in your code)

    players = [
        # ... (add your player instances here)
    ]

weights = [1 if player.ovr <= 70 else 0.5 for player in Player.players]

class RandomPlayer(Resource):
    def get(self):
        random_player, _ = random.choices(Player.players, weights=weights)[0]
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

for player in Player.players:
    feature = [player.pac, player.sho, player.pas, player.dri, player.defe, player.phy]
    label = player.pos
    features.append(feature)
    labels.append(label)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create a Decision Tree classifier and fit it to the data
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

@app.route('/get_random_player', methods=["GET"])
def get_random_player():
    random_player = random.choices(Player.players, weights=weights)[0]
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

    # Use the ML model to predict the player's position
    features = [random_player.pac, random_player.sho, random_player.pas, random_player.dri, random_player.defe, random_player.phy]
    predicted_position = clf.predict([features])[0]
    player_info["Predicted Position"] = predicted_position

    return jsonify(player_info)


if __name__ == '__main__':
    app.run(host='localhost', port=8281)
