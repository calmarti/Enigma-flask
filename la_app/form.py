from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from la_maquina.enigma import abecedario, juego, UKW

#CREAR FUNCIÓN PARA VALIDAR QUE EL MENSAJE NO CONTIENE ESPACIOS O BIEN HACERLE UN TRIM AL VALOR UNA VEZ ENVIADO
#USAR LIBRERIA DE CSS PARA MEJORAR LA UI, EN PLAN UNA UI MÁS TIPO MÁQUINA


def isValidAlphabet(formulario, campo): #crea un custom validator de flask
    for caracter in campo.data.upper():
        if caracter ==" ":
            raise ValidationError("Escribe tu mensaje sin dejar espacios en blanco")
        elif caracter not in abecedario:
            raise ValidationError("El mensaje contiene caracteres que no pertenecen al alfabeto de Enigma")
        


class EnigmaForm(FlaskForm):
    texto_entrada  = TextAreaField('Mensaje', validators = [DataRequired('Campo requerido'), isValidAlphabet])

    texto_salida = TextAreaField('Mensaje encriptado')
    rotor1 = SelectField('Rotor 1', choices = [*juego], validators = [DataRequired('Campo requerido')])
    rotor1_ini = SelectField('Pos', choices=list(abecedario))
    rotor2 = SelectField('Rotor 2', choices = [*juego], validators = [DataRequired('Campo requerido')])
    rotor2_ini = SelectField('Pos', choices=list(abecedario))
    rotor3 = SelectField('Rotor 3', choices = [*juego], validators = [DataRequired('Campo requerido')])
    rotor3_ini = SelectField('Pos', choices=list(abecedario))
    reflector = SelectField('Reflector', choices=[*UKW], validators = [DataRequired('Campo requerido')])
    aceptar = SubmitField('Codificar')
    reiniciar = SubmitField('Reiniciar') #verificar que el Field es el correcto