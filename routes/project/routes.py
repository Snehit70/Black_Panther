from flask import render_template, request, redirect, url_for, flash
from utils.session_utils import SessionManager
from routes.project import project_bp
from services.project_service import ProjectService

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
    return render_template('project_detail.html',project=project)

@project_bp.route('/',methods=['GET'])
def list_projects():
    projects = ProjectService.get_all_projects()
    return render_template('projects.html',projects=projects)