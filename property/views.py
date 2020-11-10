from flask import Blueprint, render_template
from flask import current_app as app

property_bp = Blueprint('property', __name__, template_folder = 'templates', static_folder = 'static')

@property_bp.route('/')
def index():