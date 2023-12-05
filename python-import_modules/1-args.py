#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1  # Subtracting 1 to exclude the script name itself

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for i in range(1, num_args + 1):
        print(f"{i}: {argv[i]}")

