from os import lseek
import flask
import os
from spotify import get_spotify_artist_info
from dotenv import find_dotenv, load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Environment variables
load_dotenv(find_dotenv())

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

# create the database tables
db.create_all()

# Register Page (starting page)
@app.route("/", methods=["GET","POST"])
def register():
   if flask.request.method == "POST":
       username__register = flask.request.form.get('username__register')
       db.session.add(username__register)
       db.session.commit()

   return flask.render_template("register.html")

# Login Page (input user into database)
@app.route('/login', methods=['GET','POST'])
def login():
    return flask.render_template('login.html')

# Index Page (app page)
@app.route('/index', methods=['GET','POST'])
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    from models import Username, Artist_ID
    app.run(
        host= '0.0.0.0',
        port= int(os.getenv("PORT", 8080)),
    )
