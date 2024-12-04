# Successive Over-Relaxation (SOR) Method in Python

def sor_method(A, b, omega, x0=None, tolerance=1e-6, max_iterations=100):
    """
    Solves Ax = b using the Successive Over-Relaxation (SOR) Method.

    Parameters:
        A: 2D list or numpy array, the coefficient matrix.
        b: List or numpy array, the right-hand side vector.
        omega: Float, the relaxation factor (1 < omega < 2 for over-relaxation).
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
        x_new = np.copy(x)

        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1 - omega) * x[i] + (omega * (b[i] - s1 - s2)) / A[i][i]

        print(f"Iteration {iteration}: x = {x_new}")

        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new

        x = x_new

    raise RuntimeError("SOR method did not converge within the maximum number of iterations.")
