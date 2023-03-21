def akkerman(m, n, d):
    if m == 0:
        return (n + 1) % d
    if n == 0:
        return akkerman(m - 1, 1, d)
    return akkerman(m - 1, akkerman(m, n - 1, d), d)


a = int(input())
b = int(input())
c = int(input())
print(akkerman(a, b, c))
