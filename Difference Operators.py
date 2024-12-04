# Difference Operators in Python

def forward_difference_table(values):
    """
    Constructs a forward difference table.

    Parameters:
        values: List of y values of known points.

    Returns:
        2D list representing the forward difference table.
    """
    n = len(values)
    table = [values]

    for i in range(1, n):
        differences = [table[i - 1][j + 1] - table[i - 1][j] for j in range(n - i)]
        table.append(differences)

    return table

# Example usage
y_values = [1, 4, 9, 16]
table = forward_difference_table(y_values)
print("Forward Difference Table:")
for row in table:
    print(row)
