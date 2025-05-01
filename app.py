from flask import Flask, render_template, url_for, request, redirect, flash, session
import os
from config import Config
from extensions import db, bootstrap

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

os.makedirs(app.instance_path, exist_ok=True)

db.init_app(app)
bootstrap.init_app(app)

from models.user import User
from models.project import Project
from models.comment import Comment
from models.interest import interest
from services.project_service import ProjectService

with app.app_context():
    db.create_all()

from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.project import project_bp
from routes.comment import comment_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(project_bp, url_prefix='/projects')
app.register_blueprint(comment_bp, url_prefix='/comments')

@app.route('/')
@app.route('/index')
def index():
    featured_projects = ProjectService.get_featured_projects()
    return render_template('index.html', featured_projects=featured_projects)

@app.template_filter('title_case')
def title_case_filter(text):
    if not text:
        return ""
    
    minor_words = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 
                   'to', 'from', 'by', 'of', 'in', 'with'}
    
    words = text.split()
    result = []
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in minor_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    
    return ' '.join(result)

@app.template_filter('tech_list')
def tech_list_filter(tech_string):
    """Convert comma-separated technologies to list"""
    if not tech_string:
        return []
    return [tech.strip() for tech in tech_string.split(',')]

if __name__ == '__main__':
	app.run(debug=True)