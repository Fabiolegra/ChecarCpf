from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length,Optional
from flask_wtf.file import FileField, FileAllowed

class FormsCpf(FlaskForm):
    form_cpf = StringField("Cpf numero: ", validators=[Optional(),Length(11, 14)])
    arquivo = FileField("Arquivo txt", validators=[Optional(),FileAllowed(['TXT','txt'],'Somente arquivos txt são permitidas.')])
    #arquivo = FileField("Alterar foto de Perfil",validators=[FileAllowed(['jpeg','jpg','png'],'Somente imagens são permitidas.')])
    botao = SubmitField("Enviar")