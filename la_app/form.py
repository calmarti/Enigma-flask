from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from la_maquina.enigma import abecedario, juego, UKW

<<<<<<< HEAD
<<<<<<< HEAD



class EnigmaForm(FlaskForm):
    texto_entrada  = TextAreaField('Mensaje', validators = [DataRequired('Campo requerido')])
=======
=======
>>>>>>> 3bd4387b7509d0e00930b9aafcc101007d1dc42a
def isAlfa(formulario, campo): #crea un custom validator de flask
    for caracter in campo.data:
        if caracter not in abecedario:
            raise ValidationError ("Texto con caracteres inválidos")


class EnigmaForm(FlaskForm):
    texto_entrada  = TextAreaField('Mensaje', validators = [DataRequired('Campo requerido'), isAlfa])
<<<<<<< HEAD
>>>>>>> 3bd4387b7509d0e00930b9aafcc101007d1dc42a
=======
>>>>>>> 3bd4387b7509d0e00930b9aafcc101007d1dc42a
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