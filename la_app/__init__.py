from flask import Flask
#from flask_bootstrap import Bootstrap

app = Flask(__name__) #instancia la app
app.config['SECRET_KEY'] = 'MUYSECRETA'
#Bootstrap.app

from la_app import routes #engancha la ruta una vez creada en routes 