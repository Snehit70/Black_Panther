from flask import render_template, request, request, redirect, url_for, flash
from routes.profile import profile_bp
from services.user_service import UserService
from utils.validation_utils import ValidationUtils
from utils.session_utils import SessionManager

@profile_bp.route('/profile')
@SessionManager.login_required
def view_profile():
    user_id =SessionManager.get_current_user_id()
    user=UserService.get_user_by_id(user_id)
    return render_template('profile.html', user=user)

@profile_bp.route('/profile/edit',methods=['GET','POST'])
@SessionManager.login_required
def edit_profile():
    user_id = SessionManager.get_current_user_id()

    if request.method == "POST":
        name=request.form.get('name')
        email =request.form.get('email')
        bio = request.form.get('bio')

        name_valid, name_error =ValidationUtils.validate_name(name)
        email_valid, email_error = ValidationUtils.validate_email(email)

        if not (name_valid and email_valid):
            errors = []
            if name_error:
                errors.append(name_error)
            if email_error:
                errors.append(email_error)
            
            for error in errors:
                flash(error, 'error')
            return render_template('edit_profile.html')
        
        try:
            updated_user = UserService.update_user(
                user_id=user_id,
                name=name,
                email=email,
                bio=bio
            )
            
            if updated_user:
                flash('Profile updated successfully', 'success')
                return redirect(url_for('profile.view_profile'))
            else:
                flash('Failed to update profile', 'error')
                return render_template('edit_profile.html')
        
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('edit_profile.html')
    
    user = UserService.get_user_by_id(user_id)
    return render_template('edit_profile.html', user=user)

@profile_bp.route('/profile/change-password', methods=['GET', 'POST'])
@SessionManager.login_required
def change_password():
    user_id = SessionManager.get_current_user_id()
    
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        password_valid, password_error = ValidationUtils.validate_password(new_password)
        
        if not password_valid:
            flash(password_error, 'error')
            return render_template('change_password.html')
        
        
        if new_password != confirm_password:
            flash('New passwords do not match', 'error')
            return render_template('change_password.html')
        
        
        try:
            success = UserService.change_password(
                user_id=user_id,
                current_password=current_password,
                new_password=new_password
            )
            
            if success:
                flash('Password changed successfully', 'success')
                return redirect(url_for('profile.view_profile'))
            else:
                flash('Current password is incorrect', 'error')
                return render_template('change_password.html')
        
        except Exception as e:
            flash(f'An error occurred: {str(e)}','error')
            return render_template('change_password.html')
    
    
    return render_template('change_password.html')

@profile_bp.route('/user/<int:user_id>')
def view_user_profile(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('index'))
    return render_template('profile.html', user=user)