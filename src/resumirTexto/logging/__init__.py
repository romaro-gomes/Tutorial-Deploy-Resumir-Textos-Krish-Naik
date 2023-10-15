"""
Além desse arquivo transforma a pasta em um modulo.

Também configura a saída dos logs/regristros
"""

import os, sys, logging

logging_padronizado="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_pasta='logs'

log_caminho_do_arquivo = os.path.join(log_pasta,'logs_executados.log')
os.makedirs(log_pasta, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format= logging_padronizado,

    handlers=[
        logging.FileHandler(log_caminho_do_arquivo), #Escreve o log no arquivo
        logging.StreamHandler(sys.stdout) # Esreve o log no terminal
    ]

)

logger = logging.getLogger('resumirTextoRegistrado')