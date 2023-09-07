#!/usr/bin/python3

from sys import argv
add = 0

for a in range(1, len(argv)):
    add += int(argv[a])
print(add)
