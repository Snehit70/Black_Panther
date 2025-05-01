from models.comment import Comment
from extensions import db
from datetime import datetime, timezone
from typing import List, Optional

class CommentService:
    @staticmethod
    def add_comment(user_id: int, project_id: int, content: str) -> Optional[Comment]:
        """Add a new comment to a project"""
        if not user_id or not project_id or not content:
            return None
            
        try:
            comment = Comment(
                user_id=user_id,
                project_id=project_id,
                content=content
            )
            db.session.add(comment)
            db.session.commit()
            return comment
        except Exception:
            db.session.rollback()
            return None

    @staticmethod
    def get_project_comments(project_id: int) -> List[Comment]:
        """Get all comments for a project"""
        if not project_id:
            return []
            
        try:
            return Comment.query.filter_by(project_id=project_id)\
                            .order_by(Comment.created_at.desc())\
                            .all()
        except Exception:
            return []

    @staticmethod
    def delete_comment(comment_id: int, user_id: int) -> bool:
        """Delete a comment if user is the owner"""
        if not comment_id or not user_id:
            return False
            
        try:
            comment = Comment.query.get(comment_id)
            if comment and comment.user_id == user_id:
                db.session.delete(comment)
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def get_comment(comment_id: int) -> Optional[Comment]:
        """Get a specific comment by ID"""
        if not comment_id:
            return None
            
        try:
            return Comment.query.get(comment_id)
        except Exception:
            return None