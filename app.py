from os import lseek
import flask
from spotify import get_spotify_data
from genius import get_genius_data

data = get_spotify_data()
genius_url = get_genius_data()[0]

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.render_template("index.html", data = data, genius_url = genius_url)

app.run()