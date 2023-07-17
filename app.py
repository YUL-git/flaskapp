from flask import Flask
app = Flask(__name__)

@app.route('/https://github.com/iDolphin99')
def hello_world():
    return 'Hello, GitHub Action!'
