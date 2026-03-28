"""
Admin Controller
Routes for admin management interface
"""
from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin.route('/papers')
def papers():
    """Papers management page"""
    return render_template('papers.html')


@admin.route('/datasets')
@admin.route('/training')
@admin.route('/methods')
@admin.route('/stats')
def admin_redirect():
    """All sub-sections live in the single-page admin interface."""
    from flask import redirect
    return redirect('/admin/')
