# Simple Iteration Method in Python

def simple_iteration(func, x0, tolerance=1e-6, max_iterations=100):
    """
    Finds a fixed point of the function `func` using Fixed Point Iteration.

    Parameters:
        func: Callable, the iteration function.
        x0: Float, initial guess.
        tolerance: Float, the tolerance level for the root approximation.
        max_iterations: Int, the maximum number of iterations.

    Returns:
        Float: The approximate fixed point.
        Int: The number of iterations taken to converge.
    """
    for iteration in range(max_iterations):
        x1 = func(x0)

        print(f"Iteration {iteration}: x0 = {x0}, x1 = {x1}")

        if abs(x1 - x0) < tolerance:
            return x1, iteration

        x0 = x1

    raise RuntimeError("Maximum number of iterations reached without finding the fixed point.")
