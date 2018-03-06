from flask import Flask, render_template, url_for, redirect, flash
from forms import LoginForm
from flask_login import LoginManager, current_user, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RNG'

@app.route("/")
@app.route('/home')
def index():
    user1 = {'username': 'Boian'}
    return render_template('home.html', user=user1, title="Welcome!")

@app.route('/clubplans')
def clubplans():
    message = "Hello, Subscriber!"
    return render_template('clubplans.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me = {}".format(form.username.data, form.remember_me.data))
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

app.run()