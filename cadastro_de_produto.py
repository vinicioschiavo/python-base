#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__ = "0.1.0"

# produto_nome = "Caneta"
# produto_cor1 = "azul"
# produto_cor2 = "branco"
# produto_preco = 3.23
# produto_dimensao_altura = 12.1
# produto_dimensao_largura = 0.8
# produto_em_estoque = True
# produto_codigo = 45678
# produto_codebar = None

# compra = ("Goku", produto_nome, 3)
# total_compra = compra[2] * produto_preco

# print(
#     f"O cliente {compra[0]} comprou a {compra[1]}"
#     f" e pagou o total de {total_compra}"
# )

# Ou pode ser feito usando o dicionario com listas
produto = {
"nome": "Caneta",
"cores": ["azul", "branco"],
"preco": 3.23,
"dimensao": {
    "altura": 12.1,
    "largura": 0.8,
},
"em_estoque": True,
"codigo": 45678,
"codebar": None,
}

cliente = {
    "nome": "Goku"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']} comprou 3 unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
