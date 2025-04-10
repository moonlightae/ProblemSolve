K = int(input())

DP = [[0, 0]] * K
DP[0] = [0, 1]
for i in range(1, K):
    DP[i] = [DP[i-1][1], DP[i-1][0] + DP[i-1][1]]

print(*DP[K-1])