from app import db
class Username(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   username = db.Column(db.String(80), unique=True)

class Artist_ID(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.column(db.String(80))
    artist_name = db.Column(db.String(120), unique=True)