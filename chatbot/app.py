from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test')
def test():
    return "test"

@app.route('/index')
def index():
    return 'index'
    
if __name__ == '__main__':
    app.run()
