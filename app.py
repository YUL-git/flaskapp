from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, GitHub Action!\n I'm studing docker and kubenetes!'
