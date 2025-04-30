from flask import render_template,request,redirect,url_for,flash
from routes.auth import auth_bp
from services.auth_service import AuthService
from utils.validation_utils import ValidationUtils
from utils.session_utils import SessionManager

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method =='POST':
        username =request.form.get('username')
        name=request.form.get('name')
        email=request.form.get('email')
        password= request.form.get('password')

        username_valid, username_error =ValidationUtils.validate_username(username)
        email_valid, email_error = ValidationUtils.validate_email(email)
        password_valid, password_error = ValidationUtils.validate_password(password)


        if not (username_valid and email_valid and password_valid):
            errors =[]
            if username_error:
                errors.append(username_error)
            if email_error:
                errors.append(email_error)
            if password_error:
                errors.append(password_error)

            
            for error in errors:
                flash(error,'error')
            return render_template('register.html')
        
        try:
            user= AuthService.register_user(
                username=username,
                name=name,
                email=email,
                password=password
            )

            if user:
                flash('Registration sucessful! Please log in,','success')
                return redirect(url_for('auth.login')) 
                
            else:
                flash('Registration failed. Please try again.','error')
                return render_template('register.html')
            
        except Exception as e:
            flash(f'An error occurred:{str(e)}','error')
            return render_template('register.html')
        

    return render_template('register.html')

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form.get('username')
        password =request.form.get('password')

        if not username_or_email or not password:
            flash('Username/Email and password are required','error')
            return render_template('login.html')

        
        try:
            user=AuthService.login(username_or_email,password)

            if user:
                SessionManager.login_user(user)
                flash('Login successful!','success')
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials','error')
                return render_template('login.html')
            
        except Exception as e:
            flash(f'An error occurred:{str(e)}','error')
            return render_template('login.html')
        
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    SessionManager.logout_user()
    flash('You have been logged out','success')
    return redirect(url_for('auth.login'))

