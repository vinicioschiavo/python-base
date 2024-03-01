#!/usr/bin/env python3
"""Imprime a mensagem de um email

NÂO MANDE SPAM!!!
"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0] 
templatename = arguments[1]   

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

for line in open(filepath):
    name, email = line.split(",")

    #TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        %  {
            "nome": name,
            "produto": "caneta",
            "texto": "Escreve muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)