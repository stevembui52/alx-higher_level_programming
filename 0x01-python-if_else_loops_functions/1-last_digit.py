#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = ld * -1
if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
if ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
if ld != 0 and ld < 6:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
