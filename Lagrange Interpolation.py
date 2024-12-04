# Lagrange Interpolation in Python

def lagrange_interpolation(x_points, y_points, x_value):
    """
    Performs Lagrange Interpolation.

    Parameters:
        x_points: List of x values of known points.
        y_points: List of y values of known points.
        x_value: The x value to interpolate.

    Returns:
        The interpolated value at x_value.
    """
    n = len(x_points)
    interpolated_value = 0

    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x_value - x_points[j]) / (x_points[i] - x_points[j])
        interpolated_value += term

    return interpolated_value

# Example usage
x_points = [1, 2, 3]
y_points = [1, 4, 9]
x_value = 2.5
result = lagrange_interpolation(x_points, y_points, x_value)
print(f"Interpolated value at x = {x_value}: {result}")
