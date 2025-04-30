from flask import Flask, render_template,url_for,request,redirect,flash,session,request
import os
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.project import project_bp


app=Flask(__name__,instance_relative_config=True)
app.config.from_object(Config)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(project_bp, url_prefix='/projects')

os.makedirs(app.instance_path, exist_ok=True)

db=SQLAlchemy(app)

from models.user import User

with app.app_context():
	db.create_all()

@app.route('/')
def home():
	return "<h1>welcome to home page</h1>"


@app.route('/index')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)