from os import lseek
import flask
from spotify import get_spotify_data

data = get_spotify_data()

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.render_template("index.html", data = data)

app.run()