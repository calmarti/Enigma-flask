from flask import Flask

app = Flask(__name__)

@app.route('/') #user/<email>
def hello():
    return 'Hello World!'

