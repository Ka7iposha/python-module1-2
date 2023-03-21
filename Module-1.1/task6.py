def c(n):
    a = 1
    for k in range(2, n+1):
        a = a * ((n + k) / k)
    return round(a)


n = int(input())
print(c(n))
