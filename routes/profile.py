from flask import redirect, render_template, url_for, flash, request, Blueprint, session
import json

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    
    if 'username' not in session:
        return redirect(url_for('login.login'))

    return render_template('profile.html')