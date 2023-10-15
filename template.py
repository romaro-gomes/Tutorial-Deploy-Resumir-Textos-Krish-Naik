"""
O objtivo desse script é automatizar a criação da infraestrutura de pastas do projeto.

Desta forma a criação de pastas fica a cargo do python.
"""

import os
from pathlib import Path
import logging

# Essa função configura a mensagem de log. O log são mensagem sobre o processo que está sendo executado. Funcionam como um registro.
# A mensagem de logging mas comun é a de erro. Mas a outras. Como a de INFO
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

nome_do_projeto="resumirTexto"

lista_de_arqivos=[
    '.github/worflows/.gitkeep', # Este arquivo é necessário para o github actions

    f'src/{nome_do_projeto}/__init__.py', # É  pasta onde está o projeto em si.

    f'src/{nome_do_projeto}/componentes/__init__.py',

    f'src/{nome_do_projeto}/utilitarios/__init__.py',

    f'src/{nome_do_projeto}/utilitarios/comum.py',

    f'src/{nome_do_projeto}/config/__init__.py',

    f'src/{nome_do_projeto}/config/configuracao.py',

    f'src/{nome_do_projeto}/pipeline/__init__.py',

    f'src/{nome_do_projeto}/logging/__init__.py',

    f'src/{nome_do_projeto}/entidades/__init__.py',

    f'src/{nome_do_projeto}/constantes/__init__.py',
    
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'

]

for caminho_do_arquivo in lista_de_arqivos:
    caminho_do_arquivo = Path(caminho_do_arquivo) #  classe Path, permite que você lide com o padrão de / de diversos sistemas operacinais. Linux e Windows usam padroes diferentes
    pasta,nome_do_arquivo=os.path.split(caminho_do_arquivo)


    # Cria as pastas, caso ela não exista
    if pasta !="":
        os.makedirs(pasta,exist_ok=True)
        logging.info(f'Criando im diretorio:{pasta} para o arquivo {nome_do_arquivo}')
    
    # Cria o arquivo caso ele não existe ou tenha nada escrito nele
    if (not os.path.exists(caminho_do_arquivo)) or (os.path.getsize(caminho_do_arquivo) == 0):
        with open(caminho_do_arquivo,'w') as f:
            pass
            logging.info(f'Criação do arquivo vazio: {caminho_do_arquivo}')

    # Se existir, ele infromará esse logging
    else:
        logging.info(f'{caminho_do_arquivo} já existe')
        
