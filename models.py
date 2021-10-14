from sqlalchemy.sql.schema import ForeignKey
from app import db
from flask_login import UserMixin
class Username(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key = True)
   username = db.Column(db.String(80), unique=True)
   artist_id = db.relationship('Artist_ID')

class Artist_ID(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username_id = db.Column(db.Integer, db.ForeignKey('username.id'))
    artist_name = db.Column(db.String(120), unique=True)

# Create the database tables
db.create_all()