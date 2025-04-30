from flask import session
from functools import wraps
from flask import redirect, url_for, flash

class SessionManager:
    @staticmethod
    def login_user(user):
        session['user_id']=user.id
        session['username']=user.username
        session.permanent = True

    @staticmethod
    def logout_user():
        session.clear()
    
    @staticmethod
    def is_logged_in():
        return 'user_id' in session
    
    @staticmethod
    def get_current_user_id():
        return session.get('user_id')
    
    @staticmethod
    def login_required(f):
        @wraps(f)
        def decoratod_function(*args, **kwargs):
            if not SessionManager.is_logged_in():
                flash('Please log in to access this page','error')
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return decoratod_function