#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = str(number)
if int(new_number[-1]) < 6 and number > 0:
  print(f"Last digit of {number} is {new_number[-1]} and is less than 6 and not 0")
elif number < 0 and int(new_number[-1]) != 0:
    print(f"Last digit of {number} is {-int(new_number[-1])} and is less than 6 and not 0")
elif int(new_number[-1]) > 5 and number > 0:
  print(f"Last digit of {number} is {int(new_number[-1])} and is greater than 5")
else:
  print(f"Last digit of {number} is {int(new_number[-1])} and is 0")
