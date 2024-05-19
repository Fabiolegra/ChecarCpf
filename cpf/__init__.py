"""
Este módulo inicializa a aplicação Flask e carrega a configuração
a partir das variáveis de ambiente.
"""

import os
from flask import Flask
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Recuperar a chave secreta das variáveis de ambiente
SENHA_SECRETA = os.getenv("SENHA_SECRETA")

# Inicializar a aplicação Flask
app = Flask(__name__)

# Configurar a aplicação Flask com a chave secreta
app.config["SECRET_KEY"] = SENHA_SECRETA

# Importar rotas após inicializar o app para evitar importações circulares
from cpf import routes
