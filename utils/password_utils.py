import secrets
import string
import zxcvbn
from werkzeug.security import generate_password_hash, check_password_hash

class PasswordUtils:
    @staticmethod
    def generate_password(length=12,include_uppercase=True,
                          include_lowercase=True,
                          include_digits=True,
                          include_special_chars=True):
        
        character_sets=[]
        if include_uppercase:
            character_sets.append(string.ascii_uppercase)
        if include_lowercase:
            character_sets.append(string.ascii_lowercase)
        if include_digits:
            character_sets.append(string.digits)
        if include_special_chars:
            character_sets.append(string.punctuation)

        all_characters=''.join(character_sets)

        password=[]
        for charset in character_sets:
            password.append(secrets.choice(charset))

        while len(password)<length:
            password.append(secrets.choice(all_characters))

        secrets.SystemRandom().shuffle(password)

        return ''.join(password)
    
    @staticmethod
    def estimate_password_strength(password):
        return zxcvbn.zxcvbn(password)
    
    @staticmethod
    def generate_reset_token(length=32):
        return secrets.token_urlsafe(length)
    
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='pbkdf2:sha256')
    
    @staticmethod
    def verify_password(stored_password,provided_password):
        return check_password_hash(stored_password, provided_password)