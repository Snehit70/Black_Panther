from models.project import Project
from extensions import db
from typing import List, Optional

class ProjectService:
    @staticmethod
    def create_project(title, technologies, description, creator_id) -> Optional[Project]:
        try:
            if not title or not creator_id:
                return None
                
            project = Project(
                title=title,
                technologies=technologies,
                description=description,
                creator_id=creator_id
            )
            db.session.add(project)
            db.session.commit()
            return project
        except Exception:
            db.session.rollback()
            return None
        
    @staticmethod
    def get_project_by_id(project_id) -> Optional[Project]:
        if not project_id:
            return None
        return Project.query.get(project_id)

    @staticmethod
    def get_all_projects() -> List[Project]:
        return Project.query.order_by(Project.created_at.desc()).all()
    
    @staticmethod
    def get_user_projects(user_id) -> List[Project]:
        if not user_id:
            return []
        return Project.query.filter_by(creator_id=user_id).order_by(Project.created_at.desc()).all()
    
    @staticmethod
    def get_featured_projects(limit=6) -> List[Project]:
        try:
            return Project.query.order_by(Project.created_at.desc()).limit(limit).all()
        except Exception:
            return []
 
    @staticmethod
    def search_projects(query) -> List[Project]:
        if not query:
            return []
            
        try:
            search_term = f"%{query}%"
            return Project.query.filter(
                db.or_(
                    Project.title.ilike(search_term),
                    Project.description.ilike(search_term),
                    Project.technologies.ilike(search_term)
                )
            ).order_by(Project.created_at.desc()).all()
        except Exception:
            return []
    
    @staticmethod
    def delete_project(project_id, user_id) -> bool:
        if not project_id or not user_id:
            return False
            
        try:
            project = Project.query.get(project_id)
            
            if not project:
                return False
                
            if project.creator_id != user_id:
                return False
                
            db.session.delete(project)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False
    
    