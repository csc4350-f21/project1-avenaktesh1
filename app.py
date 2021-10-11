from os import lseek
import flask
import os
from spotify import get_spotify_data, get_genius_data
from dotenv import find_dotenv, load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Environment variables
load_dotenv(find_dotenv())

data = get_spotify_data()
genius_url = get_genius_data()[0]


app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

uri = os.getenv('SQLALCHEMY_DATABASE_URI')
if uri.startswith('postgres://'):
    uri = uri.replace("postgres://", 'postgresql://', 1)


app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Suppres a warning - not strictly needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class artistID(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    print(name)

db.create_all()

@app.route("/", methods=["GET","POST"])
def main():

    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        artist = artistID(name=name)

        db.session.add(artist)
        db.session.commit()

    items = artistID.query.all()
    name = []

    for item in items:
        name.append(item.name)
    
    return flask.render_template(
        "index.html",
        data = data, 
        genius_url = genius_url,
        length= len(name),
        tasks= name
    )

app.run(
    host= '0.0.0.0',
    port= int(os.getenv("PORT", 8080)),
)
# app.run()

