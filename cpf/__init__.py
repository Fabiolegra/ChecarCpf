from flask import Flask 
import os
from dotenv import load_dotenv
load_dotenv()
SENHA_SECRETA = os.getenv("SENHA_SECRETA")
app = Flask(__name__)
app.config["SECRET_KEY"] = SENHA_SECRETA
from cpf import routes
