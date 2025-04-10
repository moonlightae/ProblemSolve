T = int(input())
for _ in range(T):
    L = int(input())
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))

    DP = [[0, 0, 0] for __ in range(L + 1)]
    for i in range(1, L + 1):
        DP[i][0] = max(DP[i-1][1], DP[i-1][2])
        DP[i][1] = max(DP[i-1][0], DP[i-1][2]) + L1[i-1]
        DP[i][2] = max(DP[i-1][1], DP[i-1][0]) + L2[i-1]

    print(max(DP[L][0], DP[L][1], DP[L][2]))