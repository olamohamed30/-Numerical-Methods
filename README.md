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

These explanations should provide a clear and concise overview for your README. Let me know if you’d like further refinement!
