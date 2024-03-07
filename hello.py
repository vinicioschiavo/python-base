#!/usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:
Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_br

execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Vinicio"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Vinicio", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

# #current_language = "en_US"
# #current_language = "pt_BR"
# #current_language = "it_IT"
# current_language = os.getenv("LANG")[:5]

# msg = "Hello, World!"

# if current_language == "pt_BR":
#     msg = "Olá Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour, Monde!"    

# print(msg)

###################################################################

# #current_language = "en_US"
# #current_language = "pt_BR"
# current_language = "it_IT"
# #current_language = os.getenv("LANG", "en_US")[:5]

# msg = {
#     "en_US": "Hello World!",
#     "pt_BR": "Olá Mundo!",
#     "it_IT": "Ciao, Mondo!",
#     "es_SP": "Hola, Mundo!",
#     "fr-FR": "Bonjour, Monde!",

# }

# print(msg[current_language])

###################################################################

#current_language = "en_US"
#current_language = "pt_BR"
#current_language = "it_IT"
current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",

}

"""
# try com valor default
message = msg.get(current_language, msg["en_US"])  # Poderia ser usado esse modo mais não mostra o error.
"""

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)
# para executar com outra lingua -->  ./hello.py --lang=it_IT
# para executar com outra lingua com multiplicação -->  ./hello.py --lang=fr_FR --count=5