N = int(input())
point = [0, 0]
for _ in range(N):
    point.append(int(input()))

S = 0
DP = [[0, 0, 0] for _ in range(N+2)]

DP[2] = [point[0], point[0], 0]
for i in range(2, N+2):
    DP[i][0] = DP[i-1][2] + point[i]
    DP[i][1] = DP[i-1][0] + point[i]
    DP[i][2] = max(DP[i-1][0], DP[i-1][1])

print(max(DP[-1][0], DP[-1][1]))