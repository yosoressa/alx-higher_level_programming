#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
n = str(number)
if int(n[-1]) < 6 and number > 0:
    print(f"Last digit of {number} is {n[-1]} and is less than 6 and not 0")
elif number < 0 and int(n[-1]) != 0:
    print(
        f"Last digit of {number} is {-int(n[-1])} and is less than 6 and not 0"
    )
elif int(n[-1]) > 5 and number > 0:
    print(f"Last digit of {number} is {int(n[-1])} and is greater than 5")
else:
    print(f"Last digit of {number} is {int(n[-1])} and is 0")

