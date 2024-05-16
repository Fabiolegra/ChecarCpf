import secrets
import os
from cpf import app 
from flask import flash, redirect, url_for

class ChecarCpf:
	def __init__(self,cpf):
	    self.cpf = str(cpf)
		
	def tratamento(self):
		self.cpf = [x for x in self.cpf if x.isnumeric()]#pegar somente os numeros do 'cpf'
		self.regiao = self.cpf[8]#digito da regiao
		if len(self.cpf)==11:
		    return True, str(self.regiao)
		elif len(self.cpf)>11:
		    self.cpf[:11]#pegar os primeiros elementos 
		    return True, str(self.regiao)
		else:#se o tamanho do 'cpf' for menor que 11
		    return False
		    
	def calculo(self):
	    self.primeiros = self.cpf[:9]
	    self.verificadores = self.cpf[9:]
	    for k in range(2):
	        if k == 0:
	        	self.mult = list(range(10,1,-1))
	        if k == 1:
	        	self.mult = list(range(11,1,-1))
	        soma = 0
	        for i,num in enumerate(self.primeiros):
	            soma += int(num)*self.mult[i]
	        resto = soma % 11
	        if resto == 0 or resto ==1:
	            final = 0 
	        else:
	            final = 11 - resto
	        if final == int(self.verificadores[k]):
	            self.primeiros.append(self.verificadores[k])
	            if k==1:
	                # estilizando o cpf 000.000.000-00
	                self.primeiros.insert(3,".")
	                self.primeiros.insert(7,".")
	                self.primeiros.insert(11,"-")
	                self.cpf = ''.join(self.primeiros)
	                return True
	        else:
	            return False 
	          
	            
def check_input(form):
    """
    o que faz:
        estancia a classe ChecarCpf com o cpf do formulario
    argumentos:
        form - cpf obtido do input
    """
    if form:
        objetoCpf = ChecarCpf(form)
        if objetoCpf.tratamento():
            if objetoCpf.calculo():
                flash(f"O cpf {objetoCpf.cpf} é válido", "alert-success")
            else:
                flash("Não é um cpf válido", "alert-danger")
        else:
            flash("Não é um cpf válido", "alert-danger")
            
def check_file(form):
    """
    o que faz: 
        compara os cpfs do txt e cria dois arquivos txt dos validos e invalidos 
    argumentos:
        form - arquivo txt com cpfs
    retorno:
        arquivos txts validados e invalidos
    """                         
    arquivo = form
    nome, extensao = os.path.splitext(arquivo.filename)
    caminho_salvar, nome = nome_arquivo(nome, "principal")
    arquivo.save(caminho_salvar)
    
    #armazena em uma lista os cpf 
    with open(caminho_salvar, 'r') as arquivo:
        linhas = arquivo.readlines()
        lista = [linha.rstrip() for linha in linhas]
    site = "site do projeto: https://checarcpf.onrender.com"
    github = "codigo fonte: https://github.com/Fabiolegra/ChecarCpf"
    aparencia = "     CPF       |    Regioes     "
    invalidos = [site,github]
    validos = [site,github,aparencia]
    cpf_regioes = {
    '0': 'Rio Grande do Sul',
    '1': 'Distrito Federal, Goias, Mato Grosso, Mato Grosso do Sul e Tocantins',
    '2': 'Amazonas, Para, Roraima, Amapa, Acre e Rondonia',
    '3': 'Ceará, Maranhão e Piauí',
    '4': 'Paraiba, Pernambuco, Alagoas e Rio Grande do Norte',
    '5': 'Bahia e Sergipe',
    '6': 'Minas Gerais',
    '7': 'Rio de Janeiro e Espirito Santo',
    '8': 'São Paulo',
    '9': 'Parana e Santa Catarina'
    }
    # checa se o cpf da lista e valida ou nao adicionando ela em outra lista validos ou invalidos
    for cpf_ in lista:
        objetoCpf = ChecarCpf(cpf_)
        validacao, regiao_digito = objetoCpf.tratamento()
        if validacao:
            if objetoCpf.calculo():
                regiao = cpf_regioes[regiao_digito]
                validos.append(f"{objetoCpf.cpf} - {regiao}")#cpf formatado
            else:
                invalidos.append(cpf_)
        else:
            invalidos.append(cpf_)
            
    caminho_invalidos, nome_invalido_txt = nome_arquivo("invalidos", "invalidos")
    criar_txt(caminho_invalidos, invalidos)#criação do txt de cpf invalido
        
    caminho_validos, nome_valido_txt = nome_arquivo("validos", "validos")
    criar_txt(caminho_validos, validos)#criação do txt de cpf valido
        
    return nome_valido_txt, nome_invalido_txt
        
        
def nome_arquivo(nome,pasta):
    """
    o que faz:
        cria um caminho adicionando digitos aleatorios ao nome do arquivo e retorna o caminho e o nome do arquivo
    argumentos:
        nome : string - nome antes da alteração
        pasta : string - onde o arquivo será armazenado
    """
    codigo = secrets.token_hex(8)#criando um codigo aleatorio para não confundir arquivos de mesmos nomes
    nome = nome.replace(" ", "")#retirando o espaço em branco do nome do arquivo
    nome_do_arquivo = nome + codigo + ".txt"#criando um nome com o codigo e a extensão
    caminho = os.path.join(app.root_path,f"arquivos/{pasta}", nome_do_arquivo)#caminho onde o arquivo será salvo
    return caminho, nome_do_arquivo
    
    
def criar_txt(destino,lista):
    """
    o que faz:
        cria um txt escrevendo cada 'cpf' em uma linha
    argumentos:
        destino: string - nome do arquivo e onde ele será salvo
        lista: list - lista de cpf a serem adicionados no txt
    """
    with open(destino, "w") as arquivo:
        for item in lista:
            arquivo.write(str(item) + "\n")
        
            