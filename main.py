import os.path
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    ret = '<ul>'
    for name in os.listdir('./static/'):
        ret += f'<li><a href="./static/{name}">{name}</a></li>'
    ret += '</ul>'
    return ret

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
