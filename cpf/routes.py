from flask import render_template,flash,redirect,url_for
from cpf import app
from cpf.forms import * 
from cpf.funcoes import *

# Codigo
@app.route("/",methods=["GET","POST"])
def home():
    cpf = FormsCpf()    
    objetoCpf = ChecarCpf(cpf.cpfForm.data)
    if objetoCpf.tratamento():
        if objetoCpf.calculo():
            flash(f"O cpf {objetoCpf.cpf} é válido","alert-success")
        else:
            flash("Não é um cpf válido","alert-danger")
    else:
        flash("Não é um cpf válido","alert-danger")
    return render_template("home.html",cpf=cpf)
