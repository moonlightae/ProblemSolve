DP = [[1]]
a, b = map(int, input().split())
DP[0] += [0 for i in range(b)]
for n in range(1, a+1):
    DP.append([1])
    for k in range(1, b+1):
        DP[n].append(0)
        DP[n][k] = DP[n-1][k] + DP[n-1][k-1]
print(DP[a][b])