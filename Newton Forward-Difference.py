# Newton Forward-Difference Formula in Python

def newton_forward_interpolation(x_points, y_points, x_value):
    """
    Performs Newton Forward Interpolation.

    Parameters:
        x_points: List of x values of known points.
        y_points: List of y values of known points.
        x_value: The x value to interpolate.

    Returns:
        The interpolated value at x_value.
    """
    n = len(x_points)
    diff_table = forward_difference_table(y_points)
    h = x_points[1] - x_points[0]
    u = (x_value - x_points[0]) / h

    interpolated_value = diff_table[0][0]
    u_product = 1
    for i in range(1, n):
        u_product *= (u - i + 1) / i
        interpolated_value += u_product * diff_table[i][0]

    return interpolated_value

# Example usage
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]
x_value = 2.5
result = newton_forward_interpolation(x_points, y_points, x_value)
print(f"Interpolated value at x = {x_value}: {result}")
