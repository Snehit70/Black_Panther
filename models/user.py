from datetime import datetime
from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True, nullable=False)
    name=db.Column(db.String(120), nullable=False)
    email=db.Column(db.String(120),unique=True, nullable= False)
    password=db.Column(db.String(120), nullable=False)
    bio= db.Column(db.Text, nullable=True)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
