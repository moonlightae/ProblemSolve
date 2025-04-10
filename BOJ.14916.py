N = int(input())

if N >= 5:
    DP = [100000] * (N+1)
    DP[0] = 0
    DP[2] = 1
    DP[4] = 2
    DP[5] = 1

    for i in range(6, N + 1):
        DP[i] = min(DP[i-2], DP[i-5]) + 1
        if DP[i] == 100001:
            DP[i] = -1

    print(DP[N])
else:
    DP = [0, -1, 1, -1, 2, 1]
    print(DP[N])