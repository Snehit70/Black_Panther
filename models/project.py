from extensions import db 
from datetime import datetime,timezone

class Project(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(100), nullable= False)
    technologies = db.Column(db.Text)
    description =db.Column(db.Text)

    creator_id =db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    creator =db.relationship('User',backref='projects')

    created_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    comments = db.relationship('Comment', backref='project', lazy='dynamic')

    def __repr__(self):
        return f'<Project {self.title}>'