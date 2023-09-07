#!/usr/bin/python3
import sys

numarg = len(sys.argv) - 1
if numarg == 0:
    print(f"{numarg:d} arguments.")
elif numarg == 1:
    print(f"{numarg:d} argument:")
else:
    print(f"{numarg:d} arguments:")

for i in range(len(sys.argv)):
    if i == 0:
        continue
    print(f"{i:d}: {sys.argv[i]:s}")
