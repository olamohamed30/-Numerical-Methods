# Secant Method in Python

def secant_method(func, x0, x1, tolerance=1e-6, max_iterations=100):
    """
    Finds a root of the function `func` using the Secant Method.

    Parameters:
        func: Callable, the function for which the root is to be found.
        x0, x1: Float, initial guesses.
        tolerance: Float, the tolerance level for the root approximation.
        max_iterations: Int, the maximum number of iterations.

    Returns:
        Float: The approximate root of the function.
        Int: The number of iterations taken to converge.
    """
    for iteration in range(max_iterations):
        f_x0, f_x1 = func(x0), func(x1)
        if abs(f_x1 - f_x0) < 1e-12:
            raise ZeroDivisionError("Difference between function values is too small.")

        # Compute the next approximation
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"Iteration {iteration}: x0 = {x0}, x1 = {x1}, x2 = {x2}, f(x2) = {func(x2)}")

        if abs(x2 - x1) < tolerance:
            return x2, iteration

        # Update for the next iteration
        x0, x1 = x1, x2

    raise RuntimeError("Maximum number of iterations reached without finding the root.")
