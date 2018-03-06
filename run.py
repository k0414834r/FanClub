from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

@app.route('/index')
def index():

    user1 = {'username': 'Boian'}

    return render_template('index.html', user=user1)

@app.route('/clubplans')
def clubplans():

    message = "Hello, Subscriber!"

    return render_template('clubplans.html', message = message)

app.run()