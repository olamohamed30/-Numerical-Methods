# -Numerical-Methods  (Ola Mohamed ElMetwally)
 Numerical Methods ( dr radwa / sec3 )

### **1.2.1 Bisection Method**
The Bisection Method is a simple way to find a root of a function \( f(x) \) in a given interval \([a, b]\). It works by repeatedly dividing the interval in half and selecting the subinterval where the root lies. This is done based on the rule that the function changes sign around the root.

**Steps**:
1. Check that \( f(a) \) and \( f(b) \) have opposite signs.
2. Find the midpoint \( c = (a + b) / 2 \).
3. If \( f(c) \) is close enough to zero, \( c \) is the root.
4. Otherwise, update the interval:
   - If \( f(a) \) and \( f(c) \) have opposite signs, set \( b = c \).
   - Else, set \( a = c \).
5. Repeat until the root is found within a desired accuracy.

---

### **1.2.2 False Position Method (Regula Falsi)**  
The False Position Method is similar to the Bisection Method but is more efficient. Instead of using the midpoint, it uses a line connecting the two points \((a, f(a))\) and \((b, f(b))\) to estimate the root.

**Steps**:
1. Check that \( f(a) \) and \( f(b) \) have opposite signs.
2. Calculate the root as:
   \[
   c = a - \frac{f(a) \cdot (b - a)}{f(b) - f(a)}
   \]
3. If \( f(c) \) is close enough to zero, \( c \) is the root.
4. Update the interval as in the Bisection Method.
5. Repeat until the root is found within a desired accuracy.

---

### **1.2.3 The Secant Method**  
The Secant Method finds a root by using two previous approximations instead of an interval. It’s faster than Bisection or False Position but doesn’t always guarantee convergence.

**Steps**:
1. Start with two initial guesses, \( x_0 \) and \( x_1 \).
2. Compute the next approximation using:
   \[
   x_{n+1} = x_n - \frac{f(x_n) \cdot (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
   \]
3. Repeat until the difference between successive approximations is small enough.

---

### **1.2.4 Simple Iteration Method (Fixed Point Iteration)**  
The Simple Iteration Method solves equations by rearranging \( f(x) = 0 \) into \( x = g(x) \), where \( g(x) \) is a function designed to converge to a fixed point.

**Steps**:
1. Start with an initial guess \( x_0 \).
2. Compute the next value using \( x_{n+1} = g(x_n) \).
3. Repeat until \( |x_{n+1} - x_n| \) is smaller than the desired tolerance.

**Note**: Convergence depends on the choice of \( g(x) \) and the initial guess.

---

### **1.2.5 Newton-Raphson Method**  
The Newton-Raphson Method is a powerful technique for finding roots. It uses the function and its derivative to iteratively refine the root.

**Steps**:
1. Start with an initial guess \( x_0 \).
2. Compute the next approximation using:
   \[
   x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
   \]
3. Repeat until the difference between successive approximations is small enough.

**Advantages**:
- Fast convergence when close to the root.
- Works well for smooth functions.

**Limitations**:
- Requires the derivative \( f'(x) \).
- May fail if \( f'(x_n) = 0 \) or if the initial guess is too far from the root.
---

### **2.1 Jacobi Iterative Method**

The Jacobi Method is an iterative technique for solving \( Ax = b \). It updates each variable independently using values from the previous iteration.

**Steps**:
1. Rearrange each equation to solve for one variable in terms of the others.
2. Start with an initial guess \( x^{(0)} \).
3. Compute the next approximation:
   \[
   x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} A_{ij} x_j^{(k)}}{A_{ii}}
   \]
4. Repeat until the solution converges.

**Advantages**:
- Easy to implement.
- Works for diagonally dominant matrices.

**Limitations**:
- Slow for large systems.
- Requires a diagonally dominant or well-conditioned matrix.

---

### **2.2 Gauss-Seidel Iterative Method**
The Gauss-Seidel Method is an improvement over the Jacobi Method. It uses the most recent updates in calculations, which often leads to faster convergence.

**Steps**:
1. Rearrange each equation to solve for one variable in terms of the others.
2. Start with an initial guess \( x^{(0)} \).
3. Compute the next approximation:
   \[
   x_i^{(k+1)} = \frac{b_i - \sum_{j < i} A_{ij} x_j^{(k+1)} - \sum_{j > i} A_{ij} x_j^{(k)}}{A_{ii}}
   \]
4. Repeat until the solution converges.

**Advantages**:
- Faster convergence than Jacobi Method.
- More efficient use of computations.

**Limitations**:
- Requires a diagonally dominant or well-conditioned matrix.

---

### **2.3 Successive Over-Relaxation (SOR) Method**
The Successive Over-Relaxation (SOR) Method improves on Gauss-Seidel by introducing a relaxation factor \( \omega \), which accelerates convergence for well-chosen \( \omega \).

**Steps**:
1. Start with an initial guess \( x^{(0)} \).
2. Compute the next approximation:
   \[
   x_i^{(k+1)} = (1 - \omega) x_i^{(k)} + \frac{\omega}{A_{ii}} \left( b_i - \sum_{j < i} A_{ij} x_j^{(k+1)} - \sum_{j > i} A_{ij} x_j^{(k)} \right)
   \]
3. Repeat until the solution converges.

**Advantages**:
- Faster convergence with an optimal \( \omega \).
- Generalized version of Gauss-Seidel.

**Limitations**:
- Requires choosing the correct \( \omega \) for efficiency.
- May not converge for poorly conditioned matrices.

---

### **3.1 Lagrange Interpolation**
Lagrange Interpolation constructs a polynomial passing through all given points.

**Steps**:
1. Use each known point \( (x_i, y_i) \) to construct a term:
   \[
   L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}
   \]
2. Multiply \( L_i(x) \) by \( y_i \) and sum them up:
   \[
   P(x) = \sum_{i=0}^n y_i \cdot L_i(x)
   \]
3. The result is the interpolated value at \( x \).

---

### **3.2 Difference Operators**

Difference Operators help compute differences between consecutive points to approximate derivatives.

**Steps for Forward Difference**:
1. Compute differences between adjacent \( y \)-values:
   \[
   \Delta y_i = y_{i+1} - y_i
   \]
2. Repeat to form higher-order differences.

---

### **3.4 Newton Forward-Difference Formula**
Newton Forward-Difference Formula approximates values near the beginning of the data.

**Formula**:
\[
P(x) = y_0 + u\Delta y_0 + \frac{u(u-1)}{2!}\Delta^2 y_0 + \dots
\]
Where \( u = \frac{x - x_0}{h} \).

---

### **3.5 Newton Backward-Difference Formula**

Newton Backward-Difference Formula approximates values near the end of the data.

**Formula**:
\[
P(x) = y_n + u\Delta y_{n-1} + \frac{u(u+1)}{2!}\Delta^2 y_{n-2} + \dots
\]
Where \( u = \frac{x - x_n}{h} \).

---
