N = int(input())
lmp = [0] * 8001
l = [0] * N
if N != 1:
    for i in range(N):
        p = int(input())
        l[i] = p
        if p >= 0:
            lmp[p + 4000] += 1
        else:
            lmp[p + 4000] += 1

    l.sort()
    # x 구하기
    alpha = sum(l)
    x = round(alpha / N)

    # y 구하기
    alpha = N//2
    y = l[alpha]

    # z 구하기
    alpha = max(lmp)
    if lmp.count(alpha) == 1:
        z = lmp.index(alpha) - 4000
    else:
        lmp[lmp.index(alpha)] = 0
        z = lmp.index(alpha) - 4000

    # u 구하기
    alpha = l[-1]
    beta = l[0]
    u = alpha - beta
else:
    x = int(input())
    y = x
    z = y
    u = 0

print(x)
print(y)
print(z)
print(u)