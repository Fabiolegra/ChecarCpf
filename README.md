## Tecnologias Utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
# Projeto Online

Este projeto também está disponível online em [https://checarcpf.onrender.com/](https://checarcpf.onrender.com/).

## Validador de CPF

Este é um projeto de validação de CPF utilizando Flask, Bootstrap e programação orientada a objetos (POO).

## Funcionalidades

- Validação de CPF inserido via formulário.
- Validação de CPFs fornecidos através de um arquivo de texto.
- Retorna dois arquivos: um contendo CPFs válidos com formatação e região, e outro com CPFs inválidos.

## Pré-requisitos

- Python 3.11.8 ou superior instalado na máquina.

## Como executar o projeto

1. Clone este repositório em sua máquina local:

    ```
    git clone https://github.com/Fabiolegra/ChecarCpf.git
    ```
    
    ou
    
    ```
    git clone git@github.com:Fabiolegra/ChecarCpf.git
    ```
    
    [Como clonar um repositório](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository?tool=desktop)

2. Navegue até o diretório do projeto:

    ```
    cd seu_repositorio
    ```

3. Instale as dependências do Python:

    ```
    pip install -r requirements.txt
    ```
4. Crie um arquivo .env na raiz do projeto e adicione
   
   ```
   SENHA_SECRETA="uma senha secreta"
   ```

5. Execute o aplicativo Flask:

    ```
    python main.py
    ```
    ou 
    ```
    flask --app main run
    ```
6. Abra seu navegador e visite `http://localhost:5000` para acessar o site.

## Uso

- Insira um CPF no formulário e clique em "Validar CPF" para verificar a validade e região do CPF.
- Para verificar vários CPFs de uma só vez, clique em "Escolher arquivo" e selecione um arquivo de texto contendo os CPFs. Em seguida, clique em "Validar CPFs do arquivo" para processar os CPFs.

## Exemplo de arquivo de texto

O arquivo .txt deve conter um CPF por linha. Por exemplo:

```
12345678901
3737374839393963bxhh276272
555.555.555-55
23456789012
34567890123
2637383837;#&#€#€@*62728256
```
O codigo checar os primeiros 11 numeros.

Sinta-se à vontade para contribuir ou reportar problemas!
