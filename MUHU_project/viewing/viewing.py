from flask import Blueprint, render_template
from flask import current_app as app

viewing_bp = Blueprint('viewing_bp', __name__, template_folder = 'templates', static_folder = 'static')

@viewing_bp.route('/')
def index():
    return "View the property"