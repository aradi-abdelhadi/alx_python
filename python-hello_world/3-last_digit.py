#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Adjust the sign of the last digit for negative numbers
if number < 0:
    last_digit = -last_digit

# Print the result
print("Last digit of", number, "is", last_digit, end=' ')

# Check conditions for the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

