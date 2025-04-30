from models.project import Project
from app import db

class ProjectService:
    @staticmethod
    def create_project(title, technologies, description,creator_id):
        try:
            project = Project(
                title=title,
                technologies=technologies,
                description =description,
                creator_id = creator_id
            )
            db.session.add(project)
            db.session.commit()
            return project
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def get_project_by_id(project_id):
        return Project.query.get(project_id)

    @staticmethod
    def get_all_projects():
        return Project.query.order_by(Project.created_at.desc()).all()
    
    @staticmethod
    def get_user_projects(user_id):
        return Project.query.filter_by(creator_id=user_id).order_by(Project.created_at.desc()).all()
    
    @staticmethod
    def get_featured_projects(limit=6):
        return Project.query.order_by(Project.created_at.desc()).limit(limit).all()
 
    @staticmethod
    def search_projects(query):
        search_term= f"%{query}%"
        return Project.query.filter(
            db.or_(
                Project.title.ilike(search_term),
                Project.description.ilike(search_term),
                Project.technologies.ilike(search_term)
            )
        ).order_by(Project.created_at.desc()).all()
    
    