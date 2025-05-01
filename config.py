import os 

class Config:
    BASE_DIR=os.path.abspath(os.path.dirname(__file__))
    
    INSTANCE_DIR=os.path.join(BASE_DIR,'instance')
    os.makedirs(INSTANCE_DIR, exist_ok=True)

    SQLALCHEMY_DATABASE_URI=f'sqlite:///{os.path.join(INSTANCE_DIR,"database.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    SECRET_KEY='snehit'
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE ='Lax'