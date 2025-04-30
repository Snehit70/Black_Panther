from  extensions import db
from datetime import datetime, timezone

interest = db.Table('interest',
    db.Column('user_id',db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id',db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('created_at', db.DateTime, default=lambda:datetime.now(timezone.utc))
    
                   
                   
                   
                   
                   )