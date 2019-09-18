#!/usr/bin/env python

text = "Dies ist ein Übungstext."

with open("tv_enc.txt", "w", encoding="UTF-8") as f:
    f.write(text)

with open("tv_enc.txt", "r", encoding="UTF-8") as f:
    print(f.read(-1))