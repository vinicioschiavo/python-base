#!/usr/bin/env python3

"""
Exibir relatorio de crianças matriculadas em cada atividade.

Imprimir a lista de crianças agrupadas por sala que frequentas
cada uma das atividades.
"""
__version__ = "0.1.0"

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

# Lista de alunos em cada atividade por sala "exemplo com so a aula de ingles"
# aula_ingles_sala1 = []
# aula_ingles_sala2 = []

# for aluno in aula_ingles:
#     if aluno in sala1:
#         aula_ingles_sala1.append(aluno)
#     elif aluno in sala2:
#         aula_ingles_sala2.append(aluno)

# print("Ingles sala1 ", aula_ingles_sala1)
# print("Ingles sala2 ", aula_ingles_sala2)

# Lista de alunos em cada atividade por sala "usando todos as aulas"

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)

