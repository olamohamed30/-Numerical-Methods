# -Numerical-Methods
 Numerical Methods / dr radwa sec3 

#### **1.2.1 Bisection Method**
The Bisection Method is a numerical technique used to find the root of a continuous function \( f(x) \) within a given interval \([a, b]\). This method is based on the Intermediate Value Theorem, which states that if \( f(a) \) and \( f(b) \) have opposite signs, there exists at least one root in the interval.

**Algorithm**:
1. **Initial Check**:
   - Verify that the function \( f(x) \) has opposite signs at \( a \) and \( b \), i.e., \( f(a) \cdot f(b) < 0 \). If not, the method cannot be applied.

2. **Iteration**:
   - Compute the midpoint of the interval:  
     \[
     c = \frac{a + b}{2}
     \]
   - Evaluate \( f(c) \).
   - If \( |f(c)| < \text{tolerance} \), stop and return \( c \) as the root.
   - Otherwise, update the interval:
     - If \( f(a) \cdot f(c) < 0 \), set \( b = c \).
     - Otherwise, set \( a = c \).

3. **Repeat**:
   - Continue this process until the interval size or \( |f(c)| \) is smaller than the specified tolerance, or the maximum number of iterations is reached.

**Key Advantages**:
- Guaranteed to converge if the initial interval is valid.
- Simple and robust.

**Limitations**:
- Slow convergence compared to other methods.
- Requires the function to change signs within the interval.

