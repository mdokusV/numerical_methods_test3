import sympy as sp


def newtons_method(f: sp.Expr, x: sp.Symbol, x0, max_error):
    """Newton's method for finding roots of a function.

    Args:
        f (sympy.Expr): The function to find the root of.
        x (sympy.Symbol): The variable symbol for the root.
        x0 (float): The initial guess for the root.
        max_error (float): The maximum error allowed.

    Returns:
        tuple: A tuple containing the approximate root value and the number of steps taken.
    """
    f_prime = f.diff(x)
    steps = 0
    x_value = x0

    while True:
        fx = f.subs(x, x_value)
        if abs(fx) < max_error:
            return x_value.evalf(), steps

        fpx = f_prime.subs(x, x_value)
        if fpx == 0:
            raise ValueError(
                "Divide by zero error. Newton's method cannot proceed.")

        x_value = x_value - fx / fpx
        steps += 1


# Define the function
x = sp.Symbol('x')
f = x**2 - 7

# Set the initial guess and maximum error
x0 = 1  # initial guess for the root
max_error = 0.0001  # maximum error allowed

# Apply Newton's method
root, steps = newtons_method(f, x, x0, max_error)
print("Approximate Root:", root)
print("Number of Steps:", steps)
print("Value of Function at Root:", f.subs(x, root).evalf())
