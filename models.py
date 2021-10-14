from app import db
from flask_login import UserMixin
class Username(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key = True)
   username = db.Column(db.String(80), unique=True)

class Artist_ID(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.column(db.String(80))
    artist_name = db.Column(db.String(120), unique=True)

# Create the database tables
db.create_all()