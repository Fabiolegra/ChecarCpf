"""
Modulo que reune todas as funções do projeto.
"""
import secrets
import os
from flask import flash
from cpf import app

class ChecarCpf:
    """
    Classe para checar e validar números de CPF brasileiros.
    """

    def __init__(self, cpf):
        """
        Inicializa com o número de CPF fornecido.
        """
        self.cpf = str(cpf)
        self.regiao = None
        self.primeiros = []
        self.verificadores = []
        self.mult = []

    def tratamento(self):
        """
        Processa o CPF para garantir que está no formato correto e determina sua região.
        """
        self.cpf = [x for x in self.cpf if x.isnumeric()]
        self.regiao = self.cpf[8] if len(self.cpf) >= 9 else None
        if len(self.cpf) == 11:
            return True, str(self.regiao)
        if len(self.cpf) > 11:
            self.cpf = self.cpf[:11]
            return True, str(self.regiao)
        return False, None

    def calculo(self):
        """
        Calcula e valida os dígitos verificadores do CPF.
        """
        self.primeiros = self.cpf[:9]
        self.verificadores = self.cpf[9:]
        for k in range(2):
            self.mult = list(range(10 + k, 1, -1))
            soma = sum(int(num) * self.mult[i] for i, num in enumerate(self.primeiros))
            resto = soma % 11
            final = 0 if resto in (0, 1) else 11 - resto
            if final == int(self.verificadores[k]):
                self.primeiros.append(self.verificadores[k])
                if k == 1:
                    self.primeiros.insert(3, ".")
                    self.primeiros.insert(7, ".")
                    self.primeiros.insert(11, "-")
                    self.cpf = ''.join(self.primeiros)
                    return True
            else:
                return False
        return False

def cpf_regioes(regiao_digito):
    """
    Verifica a região do CPF.
    """
    regioes = {
        '0': 'Rio Grande do Sul',
        '1': 'Distrito Federal, Goias, Mato Grosso, Mato Grosso do Sul e Tocantins',
        '2': 'Amazonas, Para, Roraima, Amapa, Acre e Rondonia',
        '3': 'Ceara, Maranhao e Piaui',
        '4': 'Paraiba, Pernambuco, Alagoas e Rio Grande do Norte',
        '5': 'Bahia e Sergipe',
        '6': 'Minas Gerais',
        '7': 'Rio de Janeiro e Espirito Santo',
        '8': 'Sao Paulo',
        '9': 'Parana e Santa Catarina'
    }
    return regioes[regiao_digito]

def check_input(form):
    """
    Verifica um único CPF inserido em um formulário.
    """
    if form:
        objeto_cpf = ChecarCpf(form)
        validacao, regiao_digito = objeto_cpf.tratamento()
        if validacao:
            if objeto_cpf.calculo():
                flash(f"O CPF {objeto_cpf.cpf} é válido, e a região é {cpf_regioes(regiao_digito)}",
                "alert-success")
            else:
                flash("Não é um CPF válido", "alert-danger")
        else:
            flash("Tratamento: Não é um CPF válido", "alert-danger")

def check_file(form):
    """
    Verifica um arquivo contendo múltiplos números de CPF.
    """
    arquivo = form
    nome, _ = os.path.splitext(arquivo.filename)
    caminho_salvar, _ = nome_arquivo_unico(nome, "principal")
    arquivo.save(caminho_salvar)

    cpfs = ler_cpfs_do_arquivo(caminho_salvar)
    validos, invalidos = processar_cpfs(cpfs)

    caminho_invalidos, nome_invalido_txt = nome_arquivo_unico("invalidos", "invalidos")
    criar_txt(caminho_invalidos, invalidos)

    caminho_validos, nome_valido_txt = nome_arquivo_unico("validos", "validos")
    criar_txt(caminho_validos, validos)

    return nome_valido_txt, nome_invalido_txt

def ler_cpfs_do_arquivo(caminho):
    """
    Lê os CPFs de um arquivo e retorna uma lista de CPFs.
    """
    with open(caminho, 'r', encoding='utf-8') as file:
        return [linha.rstrip() for linha in file.readlines()]

def processar_cpfs(lista):
    """
    Processa a lista de CPFs, separando-os em válidos e inválidos.
    """
    site = "site do projeto: https://checarcpf.onrender.com"
    github = "codigo fonte: https://github.com/Fabiolegra/ChecarCpf"
    aparencia = "     CPF       |    Regioes     "
    invalidos = [site, github,"\n"]
    validos = [site, github,"\n", aparencia]
    for cpf_ in lista:
        objeto_cpf = ChecarCpf(cpf_)
        validacao, regiao_digito = objeto_cpf.tratamento()
        if validacao:
            if objeto_cpf.calculo():
                regiao = cpf_regioes(regiao_digito)
                validos.append(f"{objeto_cpf.cpf} - {regiao}")
            else:
                invalidos.append(cpf_)
        else:
            invalidos.append(cpf_)

    return validos, invalidos

def nome_arquivo_unico(nome, pasta):
    """
    Gera um nome de arquivo único e retorna o caminho completo e o nome do arquivo.
    """
    codigo = secrets.token_hex(8)
    nome = nome.replace(" ", "")
    nome_do_arquivo = f"{nome}{codigo}.txt"
    caminho = os.path.join(app.root_path, f"arquivos/{pasta}", nome_do_arquivo)
    return caminho, nome_do_arquivo

def criar_txt(destino, lista):
    """
    Cria um arquivo de texto no destino especificado com o conteúdo da lista fornecida.
    """
    with open(destino, "w", encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")
