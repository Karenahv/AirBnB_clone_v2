#!/usr/bin/python3
""" Hello world in flask"""


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world(path=None):
    """route index"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb(path=None):
    return 'HBNB'

app.url_map.strict_slashes = False
if __name__ == '__main__':
    app.run(host='0.0.0.0')
