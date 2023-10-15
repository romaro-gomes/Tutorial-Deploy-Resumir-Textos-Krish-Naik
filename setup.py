"""
Esse script configura as propriedas do pacote que estamos criando.
A ideia de um pacote é armaazenar um conjunto de funções, classes e aplicações.
Isso agiliza o desensolvimento de projetos, pos diminuia a repetição.

Esse pacote terá informações do repositório que ele é conectado.
Os Dados do desenvolvedor.
E sua versão.

Graças a tag -e . no final de requirements. É possivél modificar os projeto sem reinstalara todas as bibliotecas


'-e, --editable <path/url>

    Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path or a VCS url.
'
fonte: https://pip.pypa.io/en/stable/cli/pip_install/


"""

import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_description= f.read()

__version__='0.0.0'

NOME_DO_REPOSITORIO="Tutorial-Deploy-Resumir-Textos-Krish-Naik"
USUARIO_DO_AUTOR='romario-gomes'
SRC_REPO='resumirTexto'
EMAIL_DO_AUTOR='romario.j.gomes@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USUARIO_DO_AUTOR,
    author_email=EMAIL_DO_AUTOR,
    description="reprodução de um CNN app",
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{USUARIO_DO_AUTOR}/{NOME_DO_REPOSITORIO}',
    project_urls={
        'Bug Tracker':f'https://github.com/{USUARIO_DO_AUTOR}/{NOME_DO_REPOSITORIO}/issues'
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)