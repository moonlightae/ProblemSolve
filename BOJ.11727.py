N = int(input())
a = 10007
dp = [0] * (N + 2)
dp[0] = 1
dp[1] = 3
for i in range(2, N):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % a
print(dp[N-1])