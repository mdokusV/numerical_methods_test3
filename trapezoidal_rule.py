def trapezoidal_rule(f, a, b, h):
    """Trapezoidal rule for numerical integration.

    Args:
        f (function): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        h (float): The step size.

    Returns:
        float: The approximate value of the integral.
    """
    n = int((b - a) / h)
    x = [a + i * h for i in range(n + 1)]
    y = [f(x_i) for x_i in x]

    integral = (y[0] + y[n]) / 2
    for i in range(1, n):
        integral += y[i]

    integral *= h
    return integral


def f(x):
    return x**2


a = 0  # lower limit of integration
b = 1  # upper limit of integration
h = 0.2  # step size

approximation = trapezoidal_rule(f, a, b, h)
print("Approximation:", approximation)
