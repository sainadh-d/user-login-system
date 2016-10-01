from flask import Flask, session, redirect, url_for, escape, request, render_template
from login import app
from user_manager import UserManager


# URL Routers
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    username_session = escape(session['username']).capitalize()
    return render_template('index.html', session_user_name=username_session)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    error = None
    try:
        if request.method == 'POST':
            username_form  = request.form['username']
            password_form  = request.form['password']

            auth_success = UserManager.authenticate(username_form, password_form)
            if auth_success:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            else:
                raise Exception('Invalid Username or password')
    except Exception as e:
        error = str(e)

    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('index'))

    msg = None
    try:
        if request.method == 'POST':
            username_form  = request.form['username']
            password_form  = request.form['password']
            email_form = request.form['email']
            if UserManager.user_exists(username_form):
                msg = 'User already exists'
            else:
                if UserManager.add_user(username_form, password_form, email_form):
                    msg = 'Registration Succesful'
                else:
                    msg = 'Registration Failed, pls try later'
    except Exception as e:
        msg = str(e)

    return render_template('register.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
