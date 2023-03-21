n = int(input())
f = [0, 1]
for i in range(n):
    if i > 1:
        f.append(f[i-1]+f[i-2])
    print(i, ' => ', f[i])
