from flask import redirect, render_template, url_for, flash, request, Blueprint
from werkzeug.security import generate_password_hash
from datetime import datetime, date
import json

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        birthday = request.form['date_of_birth']
        birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        ip = request.remote_addr


        def minmaxpassword(password):
            if len(password) < 8:
                return render_template(
                    'register.html',
                    error='Password must be at least 8 characters long'
                )
            elif len(password) > 20:
                return render_template(
                    'register.html',
                    error='Password must be no more than 20 characters long'
                )
            else:
                return True

        def minmaxusername(name):
            if len(name) < 3:
                return render_template(
                    'register.html',
                    error='Username must be at least 3 characters long'
                )
            elif len(name) > 20:
                return render_template(
                    'register.html',
                    error='Username must be no more than 20 characters long'
                )
            else:
                return True

        def emptyfield(name, password, confirm_password, email, birthday):
            if not name or not password or not confirm_password or not email or not birthday:
                return render_template(
                    'register.html',
                    error='Some fields are empty'
                )
            else:
                return True

        check_username = minmaxusername(name)
        if check_username != True:
            return check_username
        check_password = minmaxpassword(password)
        if check_password != True:
            return check_password
        check_empty = emptyfield(name, password, confirm_password, email, birthday)
        if check_empty != True:
            return check_empty

        if password != confirm_password:
            
            return render_template(
                'register.html',
                error='Passwords do not match'
            )

        now = datetime.now() 
        monthnow = now.month
        yearnow = now.year
        daynow = now.day

        year = birthday.year
        month = birthday.month
        day = birthday.day

        old = yearnow - year

        if yearnow - year < 18:
            return render_template(
                'register.html',
                error='You must be at least 18 years old to register'
            )
        elif old == 18 and monthnow < month:
            return render_template(
                'register.html',
                error='You must be at least 18 years old to register'
            )
        elif old == 18 and monthnow == month:
            if daynow < day:
                return render_template(
                    'register.html',
                    error='You must be at least 18 years old to register'
                )
        elif old == 18 and monthnow == month and daynow < day:
            return render_template(
                'register.html',
                error='You must be at least 18 years old to register'
            )

        password = generate_password_hash(password)
        
        datasav = {
            "name": name,
            "password": password,
            "email": email,
            "date_of_birth": birthday.strftime('%Y-%m-%d')
        }

        with open('data.json', 'r', encoding='utf-8') as arq:
            data = json.load(arq)

        for user in data:
            if user['name'] == name:
                print(f'User {ip} attempted to register a username that already exists: {name}')
                return render_template(
                    'register.html',
                    error='Username already exists'
                )

        for user in data:
            if user['email'] == email:
                print(f'User {ip} attempted to register an email that already exists: {email}')
                return render_template(
                    'register.html',
                    error='Email already exists'
                )

        data.append(datasav)

        with open('data.json', 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)

        print(f'The user: {ip}, successfully registered the username: {name}')
        return redirect(url_for('login.login'))
    return render_template('register.html')