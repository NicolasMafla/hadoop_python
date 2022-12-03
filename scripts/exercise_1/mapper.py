#!/usr/bin/python
import sys

for line in sys.stdin:
    person, spent = line.split()
    info = dict()
    print(f"{person}:{spent}")
