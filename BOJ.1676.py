def facto(n):
    DP = [1]
    for i in range(1, n + 1):
        DP.append(DP[i-1] * i)

    return DP[n]


N = int(input())
alpha = str(facto(N))
a = 0
for i in range(len(alpha)):
    if alpha[-i-1] != '0':
        print(a)
        break
    else:
        a += 1