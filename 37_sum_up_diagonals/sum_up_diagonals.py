def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # alternating between odds and evens starting with odds then going to evens
    length = len(matrix)
    return sum(
        # [values[i] for i, values in [*enumerate(matrix), *enumerate(reversed(matrix))]]
        [matrix[i][i] + matrix[length - 1 - i][i] for i in range(length)]
    )


if __name__ == "__main__":
    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(sum_up_diagonals(m2))

# [
#     (0, [1, 2, 3]),
#     (1, [4, 5, 6]),
#     (2, [7, 8, 9]),
#     (0, [7, 8, 9]),
#     (1, [4, 5, 6]),
#     (2, [1, 2, 3]),
# ]
