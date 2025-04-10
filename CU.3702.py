a, b = map(int, input().split())

DP = [[1 for i in range(b)] for j in range(a)]

for i in range(1, a):
    for j in range(1, b):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1])%100000000

print(DP[a-1][b-1])