N = int(input())
DP = [0] * N

if N > 4:
    DP[0] = 1
    DP[1] = 1

    for i in range(2, N):
        DP[i] = DP[i - 1] + DP[i - 2]
    print(3 * DP[-1] + 2 * DP[-2] + 2 * DP[-3] + DP[-4])
else:
    if N == 1:
        print(4)
    if N == 2:
        print(6)
    if N == 3:
        print(10)
    if N == 4:
        print(16)