def composite_simpsons_1_3(f, a, b, h):
    """Composite Simpson's 1/3 rule for numerical integration.

    Args:
        f (function): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.

    Returns:
        float: The approximate value of the integral.

    Raises:
        ValueError: If the step size is not even.
    """
    n = int((b - a) / h)
    if n % 2 != 0:
        raise ValueError("The step size must be even.")

    x = [a + i * h for i in range(n + 1)]
    y = [f(x_i) for x_i in x]

    integral = y[0] + y[n]
    for i in range(1, n, 2):
        integral += 4 * y[i]
    for i in range(2, n-1, 2):
        integral += 2 * y[i]

    integral *= h / 3
    return integral


def f(x):
    return pow(x, 4) + 1

a = 0  # lower limit of integration
b = 1  # upper limit of integration
h = 1/8  # step size

approximation = composite_simpsons_1_3(f, a, b, h)
print("Approximation:", approximation)

