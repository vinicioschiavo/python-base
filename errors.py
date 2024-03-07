#!/usr/bin/env python3

import os
import sys

# EAFP = Easy to Ask forgiveness than permission
# É mais fácil perdir perdão do que permissão

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:  # capturando a exception
    print(f"{str(e)}.")  # tratando a exception
    sys.exit(1)
else:
    print("Sucesso!!!")  # executa apenas quando não há exception
finally:
    print("Execute isso sempre!")  # executa sempre mesmo que tenha exception