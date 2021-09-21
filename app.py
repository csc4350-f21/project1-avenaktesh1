from flask import Flask
from flask.templating import render_template
from spotify import get_spotify_data

app = Flask(__name__)

@app.route("/")
def index(name = None):
    print(get_spotify_data("US"))
    return "helloworld"
    # return render_template("index.html", name=name)

app.run()