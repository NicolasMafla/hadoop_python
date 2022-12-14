#!/usr/bin/python3.8
import sys

current_person = None
current_spent = None
max_count = None

for index, line in enumerate(sys.stdin):
    person, spent, count = line.split("\t")
    count = int(count)
    if index == 0:
        current_person = person
        current_spent = spent
        max_count = count
    if current_person == person:
        if count > max_count:
            max_count = count
            current_spent = spent
    else:
        print(f"{current_person}\t{current_spent}")
        current_person = person
        current_spent = spent
        max_count = count
print(f"{current_person}\t{current_spent}")
