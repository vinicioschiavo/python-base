"""
Repete vogais

Faça um programa que pede ao usuario que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
pyhton repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter pra sair):' Goku
'Digite uma palavra (ou enter pra sair):' <enter>
Pythoon
Gookuu
"""
words = []
while True:
    word = input("Digite uma palavra (ou enter pra sair):").strip()
    if not word:  # Condição de parada
        break
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiouãêóíá":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)      

print(*words, sep="\n")