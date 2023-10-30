from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/open_pack', methods=['GET'])
def open_pack():
    random_player = random.choices(players, weights=weights)[0]
    return jsonify({
        'name': random_player.name,
        'position': random_player.pos,
        'overall': random_player.ovr,
        'pace': random_player.pac,
        'shooting': random_player.sho,
        'passing': random_player.pas,
        'dribbling' : random_player.dri,
        'defense': random_player.defe,
        'physicality': random_player.phy

    })

if __name__ == "__main__":
    app.run()
