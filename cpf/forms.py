from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length

class FormsCpf(FlaskForm):
    cpfForm = StringField("Cpf numero: ",validators=[DataRequired(),Length(11,14)])
    botao = SubmitField("Enviar")
    