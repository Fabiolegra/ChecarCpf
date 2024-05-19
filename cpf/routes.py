"""Modulo de rotas"""
from flask import render_template, redirect, url_for, request, send_from_directory
from cpf import app
from cpf.forms import FormsCpf
from cpf.funcoes import check_input, check_file

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Rota principal que renderiza o formulário CPF e lida com a validação do CPF submetido.
    """
    cpf = FormsCpf()
    if cpf.validate_on_submit():
        check_input(cpf.form_cpf.data)
        if cpf.arquivo.data:
            validos_, invalidos_ = check_file(cpf.arquivo.data)
            return redirect(url_for("resultados", validos_=validos_, invalidos_=invalidos_))
    return render_template("form.html", cpf=cpf)

@app.route("/resultados", methods=["GET"])
def resultados():
    """
    Rota que exibe os resultados da validação do CPF.
    """
    validos_ = request.args.get('validos_')
    invalidos_ = request.args.get('invalidos_')
    return render_template("resultados.html", invalidos_=invalidos_, validos_=validos_)

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    """
    Rota que lida com o download de arquivos.
    """
    folder = 'arquivos'
    return send_from_directory(directory=folder, path=filename, as_attachment=True)
