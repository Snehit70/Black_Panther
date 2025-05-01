from app import app, db
from flask_migrate import Migrate, upgrade, init, migrate as migrate_command

from models.user import User
from models.project import Project
from models.comment import Comment
from models.interest import interest

if __name__ == '__main__':
    with app.app_context():
        pass
