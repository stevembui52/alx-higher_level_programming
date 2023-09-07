#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

numargs = len(sys.argv)

if numargs != 4:
    print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
    sys.exit(1)  
else:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = ["+", "-", "*", "/"]

    if sys.argv[2] == c[0]:
        print(f"{a:d} {c[0]} {b:d} = {add(a, b)}")
    elif sys.argv[2] == c[1]:
        print(f"{a:d} {c[1]} {b:d} = {sub(a, b)}")
    elif sys.argv[2] == c[2]:
        print(f"{a:d} {c[2]} {b:d} = {mul(a, b)}")
    elif sys.argv[2] == c[3]:
        print(f"{a:d} {c[3]} {b:d} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
