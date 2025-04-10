n =int(input())
DP = [1, 2, 4]
for i in range(3, n):
    DP.append(0)
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 1000

print(DP[n-1])
