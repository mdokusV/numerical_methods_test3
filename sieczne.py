import sympy as sp

def secant_method(f: sp.Expr, x: sp.Symbol, x0: float, x1: float, max_error: float):
    """Secant method for finding roots of a function.

    Args:
        f (sp.Expr): The function to find the root of.
        x (sp.Symbol): The variable symbol for the root.
        x0 (float): The first initial guess for the root.
        x1 (float): The second initial guess for the root.
        max_error (float): The maximum error allowed.

    Returns:
        tuple: A tuple containing the approximate root value and the number of steps taken.
    """
    steps = 0

    while True:
        fx0 = f.subs(x, x0)
        fx1 = f.subs(x, x1)
        if abs(fx1) < max_error:
            return x1.evalf(), steps

        x2 = x1 - ((x1 - x0) / (fx1 - fx0)) * fx1
        x0, x1 = x1, x2
        steps += 1


# Define the function
x = sp.Symbol('x')
f = x**2 - 7

# Set the initial guesses and maximum error
x0 = 2  # first initial guess for the root
x1 = 3  # second initial guess for the root
max_error = 0.0001  # maximum error allowed

# Apply the Secant method
root, steps = secant_method(f, x, x0, x1, max_error)
print("Approximate Root:", root)
print("Number of Steps:", steps)
print("Value of Function at Root:", f.subs(x, root).evalf())
