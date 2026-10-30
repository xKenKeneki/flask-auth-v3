from flask import redirect, render_template, url_for, flash, request, Blueprint, session
from werkzeug.security import check_password_hash
from datetime import datetime, date
import json

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        if 'username' in session:
            print('The user is logged in')
        else:
            print('The user is not logged in.')

        with open('data.json', 'r', encoding='utf-8') as arq:
            data = json.load(arq)

        for user in data:
            if (

                user['name'] == name
                and check_password_hash(user['password'], password)

            ):
                flash('Login successful!', 'success')
                session['username'] = name

                return redirect(url_for('homepage.homepage'))
                
    return render_template('login.html')