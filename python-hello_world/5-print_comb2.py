#!/usr/bin/python3

# Loop from 0 to 99 (inclusive)
for i in range(100):
    # Print the numbers with leading zeros if needed
    print("{:02d}".format(i), end=", " if i < 99 else "\n")

