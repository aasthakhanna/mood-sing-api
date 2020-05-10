import mood
from flask import Flask, jsonify
from flask_cors import CORS
from spotify_client import SpotifyClient

app = Flask(__name__)
CORS(app)

@app.route("/getColor", methods=["GET"])
def get_color():
    return jsonify({
        'color': mood.get_mood(SpotifyClient())
    })