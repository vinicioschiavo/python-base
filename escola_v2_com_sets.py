#!/usr/bin/env python3

"""
Exibir relatorio de crianças matriculadas em cada atividade.

Imprimir a lista de crianças agrupadas por sala que frequentas
cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
sala1 = ["Goku", "Videl", "Satan", "Vegeta", "Bulma", "Numero18"]
sala2 = ["Bu", "Gohan", "Bills", "Tchitchi", "Pan"]

aula_ingles = ["Goku", "Videl", "Numero18", "Bills", "Gohan"]
aula_musica = ["Goku", "Bills", "Tchitchi"]
aula_danca = ["Satan", "Bulma", "Numero18", "Gohan"]

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca),
]

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    
    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)
