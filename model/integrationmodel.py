from flask import Flask, jsonify, request
import random
from flask_cors import CORS
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)

# Define position values
# ... (same as in your code)

class Player:
    # ... (same as in your code)

    players = [
    # ... (same as in your code)
]

weights = [1 if player.ovr <= 70 else 0.5 for player, _ in players]

# Create a list of features and labels for the ML model
features = []
labels = []

for player, _ in players:
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

    # Use the ML model to predict the player's position
    features = [random_player.pac, random_player.sho, random_player.pas, random_player.dri, random_player.defe, random_player.phy]
    predicted_position = clf.predict([features])[0]
    player_info["Predicted Position"] = predicted_position

    return jsonify(player_info)

if __name__ == '__main__':
    app.run(host='localhost', port=8281)
