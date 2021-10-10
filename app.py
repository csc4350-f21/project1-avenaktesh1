from os import lseek
import flask
import os
from spotify import get_spotify_data, get_genius_data
from dotenv import find_dotenv, load_dotenv

# Environment variables
load_dotenv(find_dotenv())

data = get_spotify_data()
genius_url = get_genius_data()[0]

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

# Suppres a warning - not strictly needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def main():
    return flask.render_template("index.html", data = data, genius_url = genius_url)

app.run(
    host= '0.0.0.0',
    port= int(os.getenv("PORT", 8080)),
)
# app.run()

