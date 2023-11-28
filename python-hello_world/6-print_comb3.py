#!/usr/bin/python3

# Loop for the tens place digit (i) from 0 to 8 (inclusive)
for i in range(9):
    # Loop for the units place digit (j) from i+1 to 9 (inclusive)
    for j in range(i + 1, 10):
        # Print the combination of two digits
        print("{:d}{:d}".format(i, j), end=", " if i < 8 or j < 9 else "\n")

