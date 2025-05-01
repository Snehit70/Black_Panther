from flask import request, redirect, url_for, flash
from routes.comment import comment_bp
from services.comment_service import CommentService
from utils.session_utils import SessionManager
from flask import current_app as app
from extensions import db
@comment_bp.route('/project/<int:project_id>/comment', methods=['POST'])
@SessionManager.login_required
def add_comment(project_id):
    """Add a new comment to a project"""
    content = request.form.get('content')
    
    if not content or content.strip() == "":
        flash('Comment cannot be empty', 'error')
        return redirect(url_for('project.view_project', project_id=project_id))

    try:
        user_id = SessionManager.get_current_user_id()
        
        CommentService.add_comment(
            user_id=user_id,
            project_id=project_id,
            content=content.strip()
        )
        flash('Comment added successfully', 'success')
    
    except Exception as e:
        app.logger.error(f"Error adding comment: {str(e)}")
        flash('Error adding comment. Please try again.', 'error')

    return redirect(url_for('project.view_project', project_id=project_id))

@comment_bp.route('/project/<int:project_id>/comment/<int:comment_id>/delete', methods=['POST'])
@SessionManager.login_required
def delete_comment(project_id, comment_id):
    """Delete a comment"""
    try:
        user_id = SessionManager.get_current_user_id()
        
        if CommentService.delete_comment(comment_id, user_id):
            flash('Comment deleted successfully', 'success')
        else:
            flash('You do not have permission to delete this comment', 'error')
    
    except Exception as e:
        app.logger.error(f"Error deleting comment: {str(e)}")
        flash('Error deleting comment. Please try again.', 'error')

    return redirect(url_for('project.view_project', project_id=project_id))

@comment_bp.route('/project/<int:project_id>/comment/<int:comment_id>/edit', methods=['POST'])
@SessionManager.login_required
def edit_comment(project_id, comment_id):
    """Edit a comment"""
    content = request.form.get('content')
    
    if not content or content.strip() == "":
        flash('Comment cannot be empty', 'error')
        return redirect(url_for('project.view_project', project_id=project_id))

    try:
        user_id = SessionManager.get_current_user_id()
        comment = CommentService.get_comment(comment_id)
        
        if not comment:
            flash('Comment not found', 'error')
        elif comment.user_id != user_id:
            flash('You do not have permission to edit this comment', 'error')
        else:
            # Update the comment
            comment.content = content.strip()
            db.session.commit()
            flash('Comment updated successfully', 'success')
    
    except Exception as e:
        app.logger.error(f"Error editing comment: {str(e)}")
        flash('Error updating comment. Please try again.', 'error')

    return redirect(url_for('project.view_project', project_id=project_id))