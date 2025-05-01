from models.comment import Comment
from extensions import db
from datetime import datetime, timezone
from typing import List, Optional

class CommentService:
    @staticmethod
    def add_comment(user_id: int, project_id: int, content: str) -> Comment:
        """Add a new comment to a project"""
        try:
            comment = Comment(
                user_id=user_id,
                project_id=project_id,
                content=content
            )
            db.session.add(comment)
            db.session.commit()
            return comment
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_project_comments(project_id: int) -> List[Comment]:
        """Get all comments for a project"""
        return Comment.query.filter_by(project_id=project_id)\
                          .order_by(Comment.created_at.desc())\
                          .all()

    @staticmethod
    def delete_comment(comment_id: int, user_id: int) -> bool:
        """Delete a comment if user is the owner"""
        try:
            comment = Comment.query.get(comment_id)
            if comment and comment.user_id == user_id:
                db.session.delete(comment)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_comment(comment_id: int) -> Optional[Comment]:
        """Get a specific comment by ID"""
        return Comment.query.get(comment_id)