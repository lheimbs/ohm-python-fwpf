#!/usr/bin/env python

verlauf = "verlauf_supermarkt.txt"

def get_verlauf():
    verl = []
    with open(verlauf, "w+", encoding="UTF-8") as f:
        for line in f.readline():
            if line and not line.startswith("#"):
                verl.append(line.split(" "))
    return verl

print(get_verlauf())