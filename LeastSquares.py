# Principle of Least Squares in Python

def least_squares_linear(x, y):
    """
    Fits a straight line y = mx + c to the data using the least squares principle.

    Parameters:
        x: List or numpy array, the x-values of the data points.
        y: List or numpy array, the y-values of the data points.

    Returns:
        Tuple (m, c): The slope and intercept of the best-fit line.
    """
    import numpy as np

    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate slope (m) and intercept (c)
    m = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n)) / sum((x[i] - x_mean) ** 2 for i in range(n))
    c = y_mean - m * x_mean

    return m, c

# Example usage
x_points = [1, 2, 3, 4, 5]
y_points = [2.2, 2.8, 3.6, 4.5, 5.1]
m, c = least_squares_linear(x_points, y_points)
print(f"Best-fit line: y = {m:.2f}x + {c:.2f}")
