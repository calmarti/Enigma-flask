from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from la_maquina.enigma import abecedario, juego, UKW

def isAlfa(formulario, campo): #crea un custom validator de flask
    for caracter in campo.data:
        if caracter not in abecedario:
            raise ValidationError ("Texto con caracteres inválidos")


class EnigmaForm(FlaskForm):
    texto_entrada  = StringField('Input', validators = [DataRequired('Campo requerido'), isAlfa])
    aceptar = SubmitField('Codificar')
    texto_salida = StringField('Output')
    rotor1 = SelectField('Rotor 1', choices = [*juego], validators = [DataRequired('Campo requerido')])
    rotor1_ini = SelectField('Pos', choices=list(abecedario))
    reflector = SelectField('UKW', choices=[*UKW], validators = [DataRequired('Campo requerido')])