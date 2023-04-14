def recursive(G):
    f = lambda *args: G(f, *args)
    return f


factorial = recursive(lambda f, n: 1 if n<2 else n*f(n-1))
print(factorial(10))
