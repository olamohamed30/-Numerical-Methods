# Least Squares Method for Polynomials in Python

def least_squares_polynomial(x, y, degree):
    """
    Fits a polynomial of given degree to the data using the least squares principle.

    Parameters:
        x: List or numpy array, the x-values of the data points.
        y: List or numpy array, the y-values of the data points.
        degree: Int, the degree of the polynomial.

    Returns:
        numpy.poly1d: A polynomial function representing the best fit.
    """
    import numpy as np

    # Fit the polynomial
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)

    return polynomial

# Example usage
x_points = [1, 2, 3, 4, 5]
y_points = [1.1, 2.0, 3.3, 3.9, 5.2]
degree = 2
best_fit_poly = least_squares_polynomial(x_points, y_points, degree)
print(f"Best-fit polynomial: {best_fit_poly}")
