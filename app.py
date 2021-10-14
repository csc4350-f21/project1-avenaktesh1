from os import lseek
import flask
import os

from flask_login.utils import logout_user
from werkzeug.utils import redirect
from spotify import get_spotify_artist_info
from dotenv import find_dotenv, load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user

# Environment variables
load_dotenv(find_dotenv())

# Create flask app 
app = flask.Flask(__name__)

# Intialize SQL Alchemy Database
db = SQLAlchemy(app)

# Login Manager Instantiated
login_manager = LoginManager()
login_manager.init_app(app)



# Replace the 'postgres' uri to 'postgresql'
uri = os.getenv('SQLALCHEMY_DATABASE_URI')
if uri.startswith('postgres://'):
    uri = uri.replace("postgres://", 'postgresql://', 1)

# Set the uri to the app.config
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

# Suppress a warning - not strictly needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register Page (starting page)
@app.route("/", methods=["GET","POST"])
def register():
   if flask.request.method == "POST":
       username__register = flask.request.form.get('username__register')
       username__DB_entry = Username(username=username__register)
       db.session.add(username__DB_entry)
       db.session.commit()

   return flask.render_template("register.html")

# Flask Login
@login_manager.user_loader
def load_user(username_id):
    return Username.query.get(int(username_id))

# Login Page (input user into database)
@app.route('/login', methods=['GET','POST'])
def login():
    if flask.request.method == "POST":
        username__login = flask.request.form.get('username__login')

        username__DB_login = Username.query.filter_by(username = username__login).first()
        print(username__DB_login)

        if username__DB_login:
            login_user(username__DB_login)
            return flask.redirect('/index')
        else:
            print("Error please register an account")
    return flask.render_template('login.html')

# Flask Logout
app.route('/logout')
@login_required
def logout():
    logout_user()
    return flask.render_template('/login')

app.route('/home')
@login_required
def home():
    return 'current user is' + current_user.username

# Index Page (app page)
@app.route('/index', methods=['GET','POST'])
def index():
    if flask.request.method == "POST":
        artist_id__index = flask.request.form.get
        ('artist_id__save')
        # try:
        result = get_spotify_artist_info(artist_id__index)
        response_object = Artist_ID(username = current_user.username, artist_name = result)
        db.session.add(response_object)
        db.session.commit()
   
    artist_object = Artist_ID.query.all()
    username_object = Username.query.filter_by(username = current_user.username).first()
    # .filter_by(username = current_user.username)
    artists_lst = []
    for artist in artist_object:
        artists_lst.append(artist.artist_name)
    
    return flask.render_template(
        'index.html', 
        username = current_user.username,
        artists = artists_lst,
        length = len(artists_lst),
        username_obj = username_object
    )

if __name__ == "__main__":
    from models import Username, Artist_ID
    app.run(
        # Debug mode
        debug = True,
        host= '0.0.0.0',
        port= int(os.getenv("PORT", 8080)),
    )
