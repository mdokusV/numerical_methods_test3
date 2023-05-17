def bisection_method(f, a, b, max_error):
    """Bisection method for finding roots of a function.

    Args:
        f (function): The function to find the root of.
        a (float): The lower limit of the interval.
        b (float): The upper limit of the interval.
        max_error (float): The maximum error allowed.

    Returns:
        tuple: A tuple containing the root value and the number of steps taken.
    """
    if f(a) * f(b) >= 0:
        raise ValueError(
            "The function values at the interval endpoints must have opposite signs."
        )

    steps = 0
    while abs(b - a) / 2 >= max_error:
        c = (a + b) / 2
        if f(c) == 0:
            return c, steps
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1

    root = (a + b) / 2
    value = f(root)
    return root, value, steps


import math


def bisection_steps(a, b, error):
    """Estimates the number of steps required for the Bisection method.

    Args:
        a (float): The lower limit of the interval.
        b (float): The upper limit of the interval.
        error (float): The desired error tolerance.

    Returns:
        int: The estimated number of steps required.
    """
    return math.ceil(math.log((b - a) / error) / math.log(2)) - 1


def f(x):
    return x**2 - 2


a = 1  # lower limit of the interval
b = 2  # upper limit of the interval
max_error = 1e-6  # maximum error allowed

root, value, steps = bisection_method(f, a, b, max_error)
print("Root:", root)
print("Number of Steps:", steps)
print("Value:", value)

steps = bisection_steps(a, b, max_error)
print("Formula number of steps:", steps)
