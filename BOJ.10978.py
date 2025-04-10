T = int(input())
L = [0] * T
for i in range(T):
    L[i] = int(input())

M = max(L)
dp = [0] * M

dp[0] = 0
dp[1] = 1
for i in range(2, M):
    dp[i] = i * (dp[i-1] + dp[i-2])

for i in L:
    print(dp[i-1])
