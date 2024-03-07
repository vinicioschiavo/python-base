#!/usr/bin/env python3

#numbers = [1, 2, 3, 4, 5, 6]
# numbers = range(1, 11)

# # Interable
# for number in numbers:
#     par = number % 2 == 0
#     if par:
#      print(number)
#     else:
#        continue

#     print(f"mais codigo com {number}")


# For loops / laço for
origrinal = [1, 2, 3]
dobrada = []
for n in origrinal:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List comprehension
dobrada = [n * 2 for n in origrinal]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}
print(dados)