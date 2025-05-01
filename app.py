from flask import Flask, render_template, url_for, request, redirect, flash, session
import os
from config import Config
from extensions import db, bootstrap, migrate

# Create Flask app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

os.makedirs(app.instance_path, exist_ok=True)

# Initialize extensions
db.init_app(app)
bootstrap.init_app(app)
migrate.init_app(app, db)  # Initialize migrations

# Import models - AFTER db initialization
from models.user import User
from models.project import Project
from models.comment import Comment
from models.interest import interest

# Import and register blueprints
from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.project import project_bp
from routes.comment import comment_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(project_bp, url_prefix='/projects')
app.register_blueprint(comment_bp, url_prefix='/comments')

# Remove db.create_all() since we'll use migrations instead
# with app.app_context():
#     db.create_all()

@app.route('/')
@app.route('/index')
def index():
	from services.project_service import ProjectService
	featured_projects = ProjectService.get_featured_projects()
	return render_template('index.html', featured_projects=featured_projects)

if __name__ == '__main__':
	app.run(debug=True)