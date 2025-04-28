from flask import Flask, render_template,url_for,request,redirect,flash,session,request
import os


app=Flask(__name__)

@app.route('/')
def home():
	return "<h1>welcome to home page</h1>"


@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=="POST":
		print(f"username:{request.form['username']}\n password:{request.form['password']}")
	return render_template('login.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/project')
def project():
	return render_template('project.html')

@app.route('/create_project')
def create_project():
	return render_template('create_project.html')






if __name__ == '__main__':
	app.run(debug=True)