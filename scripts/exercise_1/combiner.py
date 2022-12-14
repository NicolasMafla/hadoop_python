#!/usr/bin/python3.8
import sys

current_person = None
current_spent = None
total = 0

for index, line in enumerate(sys.stdin):
    person, spent, count = line.strip().split("\t")
    count = int(count)
    if index == 0:
        current_person = person
        current_spent = spent
    if current_person == person and current_spent == spent:
        total += count
    else:
        print(f"{current_person}\t{current_spent}\t{total}")
        current_person = person
        current_spent = spent
        total = 1
print(f"{current_person}\t{current_spent}\t{total}")