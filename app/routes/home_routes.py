from datetime import datetime
from flask import Blueprint, render_template

home_bp=Blueprint('home', __name__, template_folder='templates')

current_year = datetime.now().year

@home_bp.route('/')  # Welcome
def index():
    return render_template('index.html', music="static/sounds/inicio.mp3", current_year=current_year)

@home_bp.route('/404')
def error404():
    return render_template('404.html'), 404 