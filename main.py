from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    with open("./static/winsetup.txt", 'r') as file:
        return file.read()

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)