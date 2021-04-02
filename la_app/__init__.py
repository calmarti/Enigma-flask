from flask import Flask

app = Flask(__name__) #instancia la app
app.config['SECRET_KEY'] = 'MUYSECRETA'
#Bootstrap.app

from la_app import routes #engancha la ruta una vez creada en routes 