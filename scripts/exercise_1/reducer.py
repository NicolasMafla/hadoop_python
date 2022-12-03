#!/usr/bin/python3.8
import sys

current_person = None
spends = []

for index, line in enumerate(sys.stdin):
    person, spent = line.split("\t")
    if index == 0:
      current_person = person
    if current_person == person:
      spends.append(int(spent.strip()))
    else:
      print(f"{current_person}\t{spends}")
      current_person = person
      spends = [int(spent.strip())]
print(f"{current_person}\t{spends}")