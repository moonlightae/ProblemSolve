n, k = map(int, input().split())
DP = [[0] * n for i in range(n)]
DP[0][0] = 1
for i in range(1, n):
    DP[i][0] = 1
    for j in range(1, n):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]
        if DP[i][j] == 0:
            break

print(DP[n-1][k-1])