from flask import Blueprint, render_template
from flask import current_app as app

applying_bp = Blueprint('applying_bp', __name__, template_folder = 'templates', static_folder = 'static')

@applying_bp.route('/')
def index():
    return render_template('apply.html')