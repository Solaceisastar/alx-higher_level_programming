#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
king = abs(number) % 10
if number < 0:
    king = -king
print("Last digit of {:d} is {} and is ".format(number, king), end="")
if king > 5:
    print("greater than 5")
elif king == 0:
    print("0")
else:
    print("less than 6 and not 0")
