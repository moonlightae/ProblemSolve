L = [int(input()) for _ in range(int(input()))]
m = max(L)
dp = [0] * (m+5)
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for i in range(5,m):
    dp[i] = dp[i-5] + dp[i-1]
for i in range(len(L)):
    print(dp[L[i]-1])