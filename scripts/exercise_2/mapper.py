#!/usr/bin/python3.8
import sys

for index, line in enumerate(sys.stdin):
    if index == 0:
        pass
    else:
        citing, citted = line.split()
        print(f"{citted}\t{citing}")
