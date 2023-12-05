#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2], [4, 5]],
        [[1, 2], [4, 5], [7, 8]],
        [[1]],
        [[1], [2], [3], [4]],
        [[]]
    ]

    for matrix in test_cases:
        new_matrix = square_matrix_simple(matrix)
        print(new_matrix)

