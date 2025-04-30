import re 
import email_validator

class ValidationUtils:
    @staticmethod
    def validate_username(username):
        if not username:
            return False,"Username cannot be empty"
        
        if len(username)<3 or len(username)>20:
            return False, "Username must be 3-20 charecters long"
        
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$',username):
            return False, "Username must start with a letter and contaion only letters, numbers and underscores"
        
        return True, None
    
    @staticmethod
    def validate_email(email):
        if  not email:
            return False, "Email cannot be empty"
        
        try:
            email_validator.validate_email(email)

            banned_domains=['tempmail.com', 'throwawaymail.com']
            domain=email.split('@')[-1]
            if domain.lower() in banned_domains:
                return False, 'Disposable email domains are not allowed'
            
            return True, None
        except email_validator.EmailNotValidError as e:
            return False, str(e)
        
    @staticmethod
    def validate_password(password):
        if not password:
            return False, "password cannot be empty"
        
        if len(password)<8 or len(password)>100:
            return False, "Password cannot be empty "
        
        if not re.search(r'[A-Z]',password):
            return False, "password must contain at least one uppercase letter"
        
        if not re.search(r'[a-z]',password):
            return False, "Password must contain at least one lowercase letter"
        
        if not re.search(r'[\d]',password):
            return False, "Password must contaion at least one number"
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
            return False, "Password must contaion at least one special charecter"
        
        return True, None 
    
    @staticmethod
    def validate_name(name):
        if not name:
            return False, "Name cannot be empty"
        
        name=name.strip()

        if len(name)< 2 or len(name) >50:
            return False, "Name must be 2-50 charecters long"
        
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$',name):
            return False, "Name can only contain letters and spaces"
        
        return True, None
    
    @staticmethod
    def sanitize_input(input_string):
        if not input_string:
            return input_string
        
        input_string=input_string.strip()

        return re.sub(r'[<>&|`]','',input_string)