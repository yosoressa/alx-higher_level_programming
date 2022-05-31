#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_name = abs(number) % 10
if number < 0:
    new_name = -new_name
print(f"Last digit of {number} is {new_name} and is ")
if new_name > 5:
    print("greater than 5")
elif new_name == 0:
    print("0")
else:
    print("less than 6 and not 0")
