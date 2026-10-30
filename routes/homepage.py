from flask import render_template, Blueprint, session, url_for, redirect

homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/')
def homepage():
    if 'username' in session:
        print('User is logged in')
    else:
        print('User is not logged in')
    
    return render_template('homepage.html')

