# Jacobi Iterative Method in Python

def jacobi_method(A, b, x0=None, tolerance=1e-6, max_iterations=100):
    """
    Solves Ax = b using the Jacobi Iterative Method.

    Parameters:
        A: 2D list or numpy array, the coefficient matrix.
        b: List or numpy array, the right-hand side vector.
        x0: List or numpy array, the initial guess (default is zeros).
        tolerance: Float, the convergence criterion.
        max_iterations: Int, maximum number of iterations.

    Returns:
        List: The approximate solution vector.
    """
    import numpy as np

    n = len(A)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)

    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        print(f"Iteration {iteration}: x = {x_new}")

        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new

        x = x_new

    raise RuntimeError("Jacobi method did not converge within the maximum number of iterations.")
