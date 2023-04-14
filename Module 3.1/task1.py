def find_root(f, x1, x2, eps):
    x = (x1 + x2) / 2
    while (f(x - eps)*f(x) > 0) and (f(x + eps)*f(x) > 0):
        if f(x) * f(x1) > 0:
            x1 = x
        else:
            x2 = x
        x = (x1 + x2) / 2
    return x


f = lambda x: (x+10)*(x-6.75)*(x-15)
r = find_root(f, 0, 10, 0.005)
print("%.2f" % r)
