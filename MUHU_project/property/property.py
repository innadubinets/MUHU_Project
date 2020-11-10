from flask import Blueprint, render_template
from flask import current_app as app

property_bp = Blueprint('property_bp', __name__, template_folder = 'templates', static_folder = 'static')

@property_bp.route('/')
def index():
        return "Aboout the property"
