H, Y = map(int, input().split())
A = 1.05
B = 1.2
C = 1.35

if Y >= 5:
    DP = [0] * (Y+1)
    DP[0] = H
    DP[1] = int(DP[0] * A)
    DP[2] = int(DP[1] * A)
    DP[3] = int(DP[0] * B)
    DP[4] = int(max(DP[3] * A, DP[1] * B))
    DP[5] = int(DP[0] * C)

    for i in range(6, Y+1):
        DP[i] = int(max(DP[i-1] * A, DP[i-3] * B, DP[i-5] * C))
    print(DP[Y])
else:
    DP = [0] * 6
    DP[0] = H
    DP[1] = int(DP[0] * A)
    DP[2] = int(DP[1] * A)
    DP[3] = int(DP[0] * B)
    DP[4] = int(max(DP[3] * A, DP[1] * B))
    DP[5] = int(DP[0] * C)
    print(DP[Y])
