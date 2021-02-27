from flask import render_template, flash
from flask import request  #instancia de un objeto request que se crea con cada petición
from la_app import app
from la_app.form import EnigmaForm

from la_maquina.enigma import Rotor, Reflector, Enigma
from la_maquina.enigma import abecedario, juego, UKW


default_rotor = Rotor(abecedario, juego['I'][0], juego['I'][1], orden=1)
default_reflector = Reflector(abecedario, UKW['B'])
enigma = Enigma(abecedario, [default_rotor], default_reflector, 'AAA')

@app.route('/', methods = ['GET', 'POST']) #crea la ruta y define métodos
def index():
    form = EnigmaForm()
    if request.method=='POST': #pasa valores del formulario guardados en form.rotor1, form.reflector, etc.
        if form.validate(): #True: si pasa la validación del formulario
            #enigma.rotores = [Rotor(abecedario, juego[form.rotor1.data][0], juego[form.rotor1.data][1], orden=1)]
            default_rotor.pareo = juego[form.rotor1.data][0]
            default_rotor._paso = juego[form.rotor1.data][1]
            #enigma.reflector = Reflector(abecedario, UKW[form.reflector.data])
            default_reflector.UKW = UKW[form.reflector.data]
            enigma.ini = form.rotor1_ini.data 
            try:
                output = enigma.codificaCadena(form.texto_entrada.data)
            except ValueError as e:
                print('Error al codificar', e)
                flash('Texto de entrada inválido') 
                output=''

            form.texto_salida.data = output
            #form.rotor1_ini.data = enigma.ini  
            form.rotor1_ini.data = enigma.abecedario[enigma.rotores[0]._ini]  
        
        return render_template("index.html", formulario = form)

    else:   #si el método es 'GET' devuelve el formulario vacío 
        return render_template("index.html", formulario = form) #por defecto busca primer argumento en folder 'templates'
                                                       

