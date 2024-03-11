"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python numeros_pares.py`
2
4
6
8
...
"""

numbers = range(1, 201)

# Interable
for number in numbers:
    par = number % 2 == 0
    if par:
     print(number)