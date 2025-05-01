from extensions import db
from models.user import User
from models.project import Project
from typing import Optional, List, Dict

class InterestService:
    @staticmethod
    def express_interest(user_id, project_id):
        try:
            user = User.query.get(user_id)
            project = Project.query.get(project_id)

            if not user or not project:
                return False
            
            if project in user.interested_projects:
                return True
                
            user.interested_projects.append(project)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            return False
        
    @staticmethod
    def remove_interest(user_id, project_id):
        try:
            user = User.query.get(user_id)
            project = Project.query.get(project_id)

            if not user or not project:
                return False
            
            if project in user.interested_projects:
                user.interested_projects.remove(project)
                db.session.commit()
                return True
            
            return False
        except Exception as e:
            db.session.rollback()
            return False
        
    @staticmethod
    def is_interested(user_id, project_id):
        try:
            user = User.query.get(user_id)
            project = Project.query.get(project_id)

            if not user or not project:
                return False
            
            return project in user.interested_projects
        except Exception:
            return False
    
    @staticmethod
    def count_interested_users(project_id):
        try:
            project = Project.query.get(project_id)

            if not project:
                return 0
            
            return project.interested_users.count()
        except Exception:
            return 0
    
