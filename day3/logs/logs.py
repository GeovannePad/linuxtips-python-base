#!/usr/bin/env python3

import os
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Boilerplate, código repetitivo
# TODO: usar função
# TODO: usar lib (loguru)

# Nossa instância de logger

log = logging.Logger(__name__, log_level)

# Level

# ch = logging.StreamHandler() # Console/terminal/strerr
#ch.setLevel(log_level)

fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10 ** 6, # 10 ** 6 bytes = 1 mb
    backupCount = 10,
)
fh.setLevel(log_level)

# Formatação

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)

fh.setFormatter(fmt)

# Destino

# log.addHandler(ch)
log.addHandler(fh)

log.critical("Erro geral ex: banco de dados sumiu")
log.error("Erro que afeta uma única execução")
log.warning("Aviso que não causa erro")
log.info("Mensagem geral para usuários")
log.debug("Mensagem pro dev, qe, sysadmin")

print("----")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    
    # stdout
    #print(f"[ERRO] Deu erro {e}")
    # stderr