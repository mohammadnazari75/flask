from shared import uuidgen

from authz import db

class User(db.Model):
    
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)