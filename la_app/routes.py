import copy
from flask import render_template, flash, redirect, url_for
from flask import request  #instancia de un objeto request que se crea con cada petición
from la_app import app
from la_app.form import EnigmaForm

from la_maquina.enigma import Rotor, Reflector, Enigma
from la_maquina.enigma import abecedario, juego, UKW


default_rotor1 = Rotor(abecedario, juego['I'][0], juego['I'][1], orden=1)
default_rotor2 = copy.deepcopy(default_rotor1)
default_rotor2.orden = 2
default_rotor3 = copy.deepcopy(default_rotor1)
default_rotor3.orden = 3
default_reflector = Reflector(abecedario, UKW['B'])
enigma = Enigma(abecedario, [default_rotor1,default_rotor2, default_rotor3], default_reflector, 'AAA')

@app.route('/', methods = ['GET', 'POST']) #crea la ruta y define métodos
def index():
    form = EnigmaForm()
    if request.method=='POST': #pasa valores del formulario guardados en form.rotor1, form.reflector, etc.
        if form.validate(): #True: si pasa la validación del formulario
            #enigma.rotores = [Rotor(abecedario, juego[form.rotor1.data][0], juego[form.rotor1.data][1], orden=1)]
            default_rotor1.pareo = juego[form.rotor1.data][0]
            default_rotor1._paso = juego[form.rotor1.data][1]

            default_rotor2.pareo = juego[form.rotor2.data][0]
            default_rotor2._paso = juego[form.rotor2.data][1]

            default_rotor3.pareo = juego[form.rotor3.data][0]
            default_rotor3._paso = juego[form.rotor3.data][1]
            #enigma.reflector = Reflector(abecedario, UKW[form.reflector.data])
            default_reflector.UKW = UKW[form.reflector.data]

            enigma.ini = form.rotor1_ini.data + form.rotor2_ini.data +form.rotor3_ini.data 
            try:
                output = enigma.codificaCadena(form.texto_entrada.data)
            except ValueError as e:
                print('Error al codificar', e)
                flash('Texto de entrada inválido') 
                output=''

            form.texto_salida.data = output
            #form.rotor1_ini.data = enigma.ini  
            form.rotor1_ini.data = enigma.abecedario[default_rotor1._ini]  
            form.rotor2_ini.data = enigma.abecedario[default_rotor2._ini]
            form.rotor3_ini.data = enigma.abecedario[default_rotor3._ini] 

        if form.reiniciar.data:
            return redirect(url_for('index')) 

        return render_template("index.html", formulario = form)


    else:   #si el método es 'GET' devuelve el formulario vacío 
        return render_template("index.html", formulario = form) #por defecto busca primer argumento en folder 'templates'




        


   
                                                       

