import math


def c(n, k):
    if 0 <= k <= n:
        if n == k:
            return 1
        return (math.factorial(n)) // (math.factorial(k) * math.factorial(n - k))
    return 0


n = int(input())
print(c(n, 2), c(n, n // 4), c(n, n // 2), c(n, n * 3 // 4), c(n, n - 2))
