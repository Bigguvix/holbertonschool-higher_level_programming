#!/usr/bin/python3
output = ""
for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in "qe":
        output += f"{ch}"
print(output, end="")
