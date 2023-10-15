"""
Estr script tem a função de armazenas as funções mais utilizadas no projeto.

Ao invés de reescrever a mesma função em vários scripts. Só precisará chama-la daqui.

@ensure_annotation permite a manipulação de verificações de forma pytonica e sucinta.
fonte:https://kislyuk.github.io/ensure/

A biblioteca box permite trabalhar com dicionarios com o uso do dot,parecido com módulos.
fonte:https://box.readthedocs.io/en/4.0/
"""

import os
from box.exceptions import BoxValueError
import yaml
from resumirTexto.logging import logger
from ensure import ensure_annotations
from box import ConfigBox #https://box.readthedocs.io/en/4.0/#configbox
from pathlib import Path
from typing import Any


@ensure_annotations
def ler_yaml(caminnho_do_yaml: Path) -> ConfigBox:
    """Lerá o yaml e returnará o conteúdo

    Argumento:
        caminho_do_yaml (str): caminho como entrada

    Mensagem: 
        ValueError: Se o yaml estiver vazio
        e: arquivo vazio/empty file

    Retorna:
        ConfigBox: ConfigBox tipo
    """

    try:
        with open(caminnho_do_yaml) as arquivo_yaml:
            conteudo = yaml.safe_load(arquivo_yaml)
            logger.info(f"arquivo yaml:{caminnho_do_yaml} carregado com sucesso")
            return ConfigBox(conteudo)
    except BoxValueError:
        raise ValueError('Arquivo yaml está vazio')
    except Exception as e:
        raise e
    

@ensure_annotations
def criar_pastas(caminhos_das_pastas: list, verbose=True):
    """
    Cria uma lista de pastas

    argumentos:
        caminhos_das_pastas (list): Lista dos caminhos das pastas
        ignore_log (bool, optional): Ignora se multiplas pastas forem criadas. Por padrão é falso/False

    Retorna:
        O arquivo criado se não existit

    Mensagem:
        O local onde o arquivo está alocado
    """

    for caminho in caminhos_das_pastas:
        os.makedirs(caminho, exist_ok=True)
        if verbose:
            logger.info(f'Pasta criada em:{caminho}')

@ensure_annotations
def retorne_tamanho(caminho: Path) -> str:
    """Retorna o tamnho em KB
    
    Argumentos:
        caminho(Path): caminho do arquivo

    Returna:
        str: tamnho em KB
    """

    tamanho_em_kb = round(os.path.getsize(caminho)/1024)
    return f"{ tamanho_em_kb} KB"