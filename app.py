from os import lseek
import flask
import os
from werkzeug.user_agent import UserAgent
from werkzeug.utils import redirect
from spotify import get_spotify_data, get_genius_data
# , get_spotify_artist
from dotenv import find_dotenv, load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for

# Environment variables
load_dotenv(find_dotenv())

# import spotify and genius data
data = get_spotify_data()
genius_url = get_genius_data()[0]

# create flask app 
app = flask.Flask(__name__)

# intialize SQL Alchemy Database
db = SQLAlchemy(app)
app.debug = True

# replace the 'postgres' uri to 'postgresql'
uri = os.getenv('SQLALCHEMY_DATABASE_URI')
if uri.startswith('postgres://'):
    uri = uri.replace("postgres://", 'postgresql://', 1)

# set the uri to the app.config
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Suppress a warning - not strictly needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class artistID(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120),  unique=True)
class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   username = db.Column(db.String(80),  unique=True)

# create the database tables 
db.create_all()

@app.route('/register', methods=['GET','POST'])
def register():
    return flask.render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():

    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        user = User(request.form.get('username'))

        db.session.add(user=user)
        db.session.commit()
    # return flask.render_template('login.html')

@app.route("/", methods=["GET","POST"])
def main():
   return flask.render_template("log-in.html")

@app.route("/index", methods=["GET","POST"])
def test():
    if flask.request.method == "POST":

        name = flask.request.form.get("name")
        artist = artistID(name='joji')

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
        length = len(name),
        name = name
    )


app.run(
    host= '0.0.0.0',
    port= int(os.getenv("PORT", 8080)),
)

# app.run()
