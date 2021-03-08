from flask import Flask
<<<<<<< HEAD
<<<<<<< HEAD

=======
#from flask_bootstrap import Bootstrap
>>>>>>> 3bd4387b7509d0e00930b9aafcc101007d1dc42a
=======
#from flask_bootstrap import Bootstrap
>>>>>>> 3bd4387b7509d0e00930b9aafcc101007d1dc42a

app = Flask(__name__) #instancia la app
app.config['SECRET_KEY'] = 'MUYSECRETA'
#Bootstrap.app

from la_app import routes #engancha la ruta una vez creada en routes 