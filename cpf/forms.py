"""Módulo de formulários para CPF."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Optional

class FormsCpf(FlaskForm):
    """
    Formulário para entrada de CPF e arquivo txt.
    """
    form_cpf = StringField(
        "Cpf numero: ", 
        validators=[Optional(), Length(11, 14)]
    )
    arquivo = FileField(
        "Arquivo txt", 
        validators=[Optional(), FileAllowed(['TXT', 'txt'], 'Somente arquivos txt são permitidas.')]
    )
    botao = SubmitField("Enviar")
