from flask import Flask
from spotify import get_spotify_data

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

app.run()