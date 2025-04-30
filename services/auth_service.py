from werkzeug.security import generate_password_hash, check_password_hash
from services.user_service import UserService
from models.user import User
from app import db
import secrets

class AuthService:
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='pbkdf2:sha256')
    
    @staticmethod
    def verify_password(stored_password,provided_password):
        return check_password_hash(stored_password, provided_password)
    
    @staticmethod
    def register_user(username,name,email,password,bio=None):
        hashed_password=AuthService.hash_password(password)

        return UserService.create_user(
            username=username,
            name=name,
            email=email,
            password=hashed_password,
            bio=bio
        )
    @staticmethod
    def login(username_or_email, password):
        user=(
            UserService.get_user_by_username(username_or_email)or 
            UserService.get_user_by_email(username_or_email)
        )

        if not user:
            return None
        
        if AuthService.verify_password(user.password,password):
            return user
        
        return None
    
    @staticmethod
    def generate_token():
        return secrets.token_hex(32)