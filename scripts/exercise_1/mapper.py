#!/usr/bin/python3.8
import sys

for line in sys.stdin:
    person, spent = line.split()
    print(f"{person}\t{spent}")
