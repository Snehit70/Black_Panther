from services.user_service import UserService
from models.user import User
from extensions import db
import secrets
from utils.password_utils import PasswordUtils

class AuthService:
   
    @staticmethod
    def register_user(username,name,email,password,bio=None):
        hashed_password=PasswordUtils.hash_password(password)

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
        
        if PasswordUtils.verify_password(user.password,password):
            return user
        
        return None
    
    @staticmethod
    def generate_token():
        return secrets.token_hex(32)