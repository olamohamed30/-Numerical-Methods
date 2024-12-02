# Bisection Method in Python

def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Finds a root of the function `func` within the interval [a, b] using the Bisection Method.

    Parameters:
        func: Callable, the function for which the root is to be found.
        a: Float, the starting point of the interval.
        b: Float, the ending point of the interval.
        tolerance: Float, the tolerance level for the root approximation.
        max_iterations: Int, the maximum number of iterations to perform.

    Returns:
        Float: The approximate root of the function.
        Int: The number of iterations taken to converge.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at points a and b.")

    iteration = 0
    while iteration < max_iterations:
        # Find the midpoint
        midpoint = (a + b) / 2.0
        mid_value = func(midpoint)

        print(f"Iteration {iteration}: a = {a}, b = {b}, midpoint = {midpoint}, f(midpoint) = {mid_value}")

        # Check if we've found the root or are within the tolerance
        if abs(mid_value) < tolerance or abs(b - a) / 2 < tolerance:
            return midpoint, iteration

        # Decide the subinterval for the next step
        if func(a) * mid_value < 0:
            b = midpoint
        else:
            a = midpoint

        iteration += 1

    raise RuntimeError("Maximum number of iterations reached without finding the root.")
