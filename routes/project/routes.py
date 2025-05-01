from flask import render_template, request, redirect, url_for, flash
from utils.session_utils import SessionManager
from routes.project import project_bp
from services.project_service import ProjectService
from services.interest_service import InterestService

@project_bp.route('/create', methods=['GET','POST'])
@SessionManager.login_required
def create_project():
    if request.method == 'POST':
        title =request.form.get('title')
        technologies = request.form.get('technologies')
        description =request.form.get('description')

        user_id = SessionManager.get_current_user_id()

        try:
            project = ProjectService.create_project(
                title = title,
                technologies = technologies,
                description = description,
                creator_id = user_id
            )
            if project:


                flash('Project created successfully', 'success')
                return redirect(url_for('project.view_project',project_id=project.id))
            else:
                flash('Failed to create a project','error')
        except Exception as e:
            flash(f'An error occurred:{str(e)}','error')

    return render_template('create_project.html')

@project_bp.route('/<int:project_id>',methods=['GET','POST'])
def view_project(project_id):
    project =ProjectService.get_project_by_id(project_id)

    if not project:
        flash('Project not found','error')
        return redirect(url_for('project.list_projects'))
    
    interest_count = InterestService.count_interested_users(project_id)

    is_interested=False
    if SessionManager.is_logged_in():
        user_id= SessionManager.get_current_user_id()
        is_interested= InterestService.is_interested(user_id, project_id)

    return render_template('project_detail.html',
                           project=project,
                           interest_count=interest_count,
                           is_interested=is_interested)

@project_bp.route('/',methods=['GET'])
def list_projects():
    projects = ProjectService.get_all_projects()
    return render_template('project.html',projects=projects)

@project_bp.route('/<int:project_id>/interest', methods=['POST'])
@SessionManager.login_required
def toggle_interest(project_id):
    user_id = SessionManager.get_current_user_id()

    try:
        if InterestService.is_interested(user_id, project_id):
            InterestService.remove_interest(user_id, project_id)
            flash('Interest removed','success')

        else:
            InterestService.express_interest(user_id, project_id)
            flash('Interest added','success')

        return redirect(url_for('project.view_project',project_id=project_id))
    except Exception as e:
        flash(f'An error occurred: {str(e)}','error')
        return redirect(url_for('project.view_project',project_id=project_id))
    
@project_bp.route('/search')
def search():
    query = request.args.get('query','')
    if not query:
        return redirect(url_for('project.list_projects'))
    
    projects = ProjectService.search_projects(query)
    return render_template('project.html',
                           projects=projects,
                           search_query=query)

@project_bp.route('/<int:project_id>/delete', methods=['POST'])
@SessionManager.login_required
def delete_project(project_id):
    user_id = SessionManager.get_current_user_id()
    
    try:
        result = ProjectService.delete_project(project_id, user_id)
        
        if result:
            flash('Project deleted successfully', 'success')
            return redirect(url_for('project.list_projects'))
        else:
            flash('Failed to delete project. You may not have permission.', 'error')
            return redirect(url_for('project.view_project', project_id=project_id))
            
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('project.view_project', project_id=project_id))