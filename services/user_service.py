from models.user import User
from app import  db
from sqlalchemy.exc import IntegrityError
from utils.password_utils import PasswordUtils

class UserService:
    @staticmethod
    def create_user(username,name,email,password,bio=None):
        try :
            if not username or not email or not password:
                raise ValueError("Missing required fields")
            
            existing_user=User.query.filter(
                (User.username==username) | (User.email==email)
            ).first()

            if existing_user:
                raise ValueError("Username or email already exists")
            
            new_user=User(
                username=username,
                name=name,
                email=email,
                password=password,
                bio=bio
            )

            db.session.add(new_user)
            db.session.commit()

            return new_user
        except(IntegrityError,ValueError) as e:
            db.session.rollback()
            print(f"Error creating user:{str(e)}")
            return None
        
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def update_user(user_id, name=None, email=None, bio=None):
        try :
            user=User.query.get(user_id)

            if not user:
                return None
            
            if name:
                user.name=name
            if email:
                user.email = email
            if bio is not None:
                user.bio = bio
            
            db.session.commit()
            return user
        
        except Exception as e:
            db.session.rollback()
            print(f"Error updating user: {str(e)}")
            return None
        
    @staticmethod
    def change_password(user_id, current_password, new_password):
        try :
            user = User.query.get(user_id)

            if not user:
                return False
            
            if not PasswordUtils.verify_password(user.password, current_password):
                return False
            
            hashed_password =PasswordUtils.hash_password(new_password)
            user.password =hashed_password

            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            print(f"Error changing password: {str(e)}")
            return False