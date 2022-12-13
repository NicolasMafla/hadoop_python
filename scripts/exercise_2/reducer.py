#!/usr/bin/python3.8
import sys

current_citted = None
cittings = set()

for index, line in enumerate(sys.stdin):
    citted, citting = line.split("\t")
    if index == 0:
        current_citted = citted
    if current_citted == citted:
        cittings.add(int(citting.strip()))
    else:
        print(f"{current_citted.strip()}\t{','.join([str(s) for s in sorted(cittings)])}")
        current_citted = citted
        cittings = [int(citting.strip())]
print(f"{current_citted.strip()}\t{','.join([str(s) for s in sorted(cittings)])}")
