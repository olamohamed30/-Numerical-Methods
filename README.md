# -Numerical-Methods
 Numerical Methods / dr radwa sec3 
 #1.2.1 Bisection Method
The Bisection Method is a numerical technique used to find the root of a continuous function 
f
(
x
)
f(x) within a given interval 
[
a
,
b
]
[a,b]. This method is based on the Intermediate Value Theorem, which states that if 
f
(
a
)
f(a) and 
f
(
b
)
f(b) have opposite signs, there exists at least one root in the interval.

Algorithm:

Initial Check:

Verify that the function 
f
(
x
)
f(x) has opposite signs at 
a
a and 
b
b, i.e., 
f
(
a
)
⋅
f
(
b
)
<
0
f(a)⋅f(b)<0. If not, the method cannot be applied.
Iteration:

Compute the midpoint of the interval:
c
=
a
+
b
2
c= 
2
a+b
​
 
Evaluate 
f
(
c
)
f(c).
If 
∣
f
(
c
)
∣
<
tolerance
∣f(c)∣<tolerance, stop and return 
c
c as the root.
Otherwise, update the interval:
If 
f
(
a
)
⋅
f
(
c
)
<
0
f(a)⋅f(c)<0, set 
b
=
c
b=c.
Otherwise, set 
a
=
c
a=c.
Repeat:

Continue this process until the interval size or 
∣
f
(
c
)
∣
∣f(c)∣ is smaller than the specified tolerance, or the maximum number of iterations is reached.
Key Advantages:

Guaranteed to converge if the initial interval is valid.
Simple and robust.
Limitations:

Slow convergence compared to other methods.
Requires the function to change signs within the interval.
