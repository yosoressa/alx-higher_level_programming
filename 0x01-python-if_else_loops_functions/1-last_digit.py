#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
new = abs(number) % 10
if number < 0:
    new = -new
print("Last digit of {} is {} and is ".format(number, new), end="")
if new > 5:
    print("greater than 5")
elif new == 0:
    print("0")
else:
    print("less than 6 and not 0")

