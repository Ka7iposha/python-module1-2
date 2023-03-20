x = int(input())
i = 0
f = []
while True:
    f.append(x)
    if (x % 2) == 0:
        x = x // 2
    elif x == 1:
        break
    else:
        x = 3 * x + 1
    print(i, ' => ', f[i])
    i += 1
f.append(1)
print(i, ' => ', f[i])

