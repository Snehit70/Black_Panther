from datetime import datetime,timezone
from extensions import db
from models.interest import interest

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True, nullable=False)
    name=db.Column(db.String(120), nullable=False)
    email=db.Column(db.String(120),unique=True, nullable= False)
    password=db.Column(db.String(120), nullable=False)
    bio= db.Column(db.Text, nullable=True)
    created_at=db.Column(db.DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at=db.Column(db.DateTime,default=lambda:datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

    interested_projects = db.relationship('Project',
                                        secondary=interest,
                                        backref=db.backref('interested_users', lazy='dynamic'))
    
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    