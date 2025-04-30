from app import db
from models.user import User
from models.project import Project

class InterestService:
    @staticmethod
    def express_interest(user_id, project_id):
        try :
            user=User.query.get(user_id)
            project=Project.query.get(project_id)

            if not user or not project:
                return False
            
            user.interested_projects.append(project)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def remove_interest(user_id, project_id):
        try:
            user = User.query.get(user_id)
            project=Project.query.get(project_id)

            if not user or not project:
                return False
            
            if project in user.interested_projects:
                user.interested_projects.remove(project)
                db.session.commit()
                return True
            
            return False
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def is_interested(user_id, project_id):
        user = User.query.get(user_id)
        project= Project.query.get(project_id)

        if not user or not project:
            return False
        
        return project in user.interested_projects
    
    @staticmethod
    def count_interested_users(project_id):
        project = Project.query.get(project_id)

        if not project:
            return 0
        
        return project.interested_users.count()
    
