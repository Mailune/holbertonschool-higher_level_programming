#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print(f"{i}{j}, " if i != 8 else f"{i}{j}\n", end="")