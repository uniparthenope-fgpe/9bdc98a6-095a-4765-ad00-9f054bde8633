import scipy.optimize as optimize


def find_minimum(equation):
    """
    Find the minimum of the given function using the scipy.optimize module.
    """

    def f(x):
        return eval(equation)

    # Use the minimize function to find the minimum of the function.
    result = optimize.minimize(f, x0=0)

    # Extract the minimum value from the result object.
    minimum = result.fun

    return minimum


func = input()
print(find_minimum(func))
