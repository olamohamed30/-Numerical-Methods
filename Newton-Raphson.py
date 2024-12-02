# Newton-Raphson Method in Python

def newton_raphson(func, derivative, x0, tolerance=1e-6, max_iterations=100):
    """
    Finds a root of the function `func` using the Newton-Raphson Method.

    Parameters:
        func: Callable, the function for which the root is to be found.
        derivative: Callable, the derivative of `func`.
        x0: Float, initial guess.
        tolerance: Float, the tolerance level for the root approximation.
        max_iterations: Int, the maximum number of iterations.

    Returns:
        Float: The approximate root of the function.
        Int: The number of iterations taken to converge.
    """
    for iteration in range(max_iterations):
        f_x0 = func(x0)
        f_prime_x0 = derivative(x0)

        if abs(f_prime_x0) < 1e-12:
            raise ZeroDivisionError("Derivative is too small.")

        x1 = x0 - f_x0 / f_prime_x0

        print(f"Iteration {iteration}: x0 = {x0}, f(x0) = {f_x0}, derivative = {f_prime_x0}, x1 = {x1}")

        if abs(x1 - x0) < tolerance:
            return x1, iteration

        x0 = x1

    raise RuntimeError("Maximum number of iterations reached without finding the root.")
