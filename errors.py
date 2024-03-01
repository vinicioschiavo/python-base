#!/usr/bin/env python3

import os
import sys

# LBYL = Look Before You Leap / Olhe antes de atreavesar

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # Race condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)
        
if len(names) >= 3 :
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)