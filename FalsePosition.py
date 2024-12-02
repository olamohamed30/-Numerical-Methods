def false_position_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Finds a root of the function `func` within the interval [a, b] using the False Position Method.

    Parameters:
        func: Callable, the function for which the root is to be found.
        a, b: Float, endpoints of the interval.
        tolerance: Float, the tolerance level for the root approximation.
        max_iterations: Int, the maximum number of iterations.

    Returns:
        Float: The approximate root of the function.
        Int: The number of iterations taken to converge.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at points a and b.")

    for iteration in range(max_iterations):
        # Calculate the point using the False Position formula
        root = a - (func(a) * (b - a)) / (func(b) - func(a))
        f_root = func(root)

        print(f"Iteration {iteration}: a = {a}, b = {b}, root = {root}, f(root) = {f_root}")

        if abs(f_root) < tolerance:
            return root, iteration

        # Update the interval
        if func(a) * f_root < 0:
            b = root
        else:
            a = root

    raise RuntimeError("Maximum number of iterations reached without finding the root.")
