from flask import Flask, render_template, url_for
from forms import LoginForm
from flask_login import current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RNG'

@app.route("/")
@app.route('/home')
def index():
    user1 = {'username': 'Boian'}
    return render_template('home.html', user=user1)

@app.route('/clubplans')
def clubplans():
    message = "Hello, Subscriber!"
    return render_template('clubplans.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

app.run()