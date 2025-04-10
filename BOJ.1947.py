N = int(input())
dp = [0] * 3

dp[0] = 0
dp[1] = 1
for i in range(2, N):
    dp[2] = (i * (dp[1] + dp[0])) % 1000000000
    dp[0], dp[1], dp[2] = dp[1], dp[2], 0

if N >= 3:
    print(dp[1])
else:
    if N == 1:
        print(0)
    else:
        print(1)