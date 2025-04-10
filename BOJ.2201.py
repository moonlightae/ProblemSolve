# 88자리까지만 구하면 된다!

N = int(input())
DP = [[[], []], [[], []]]
DP[0] = [['1'], []]
if N > 1:
    N -= 1
    sN = N
    while True:
        DP[1][1] = list(map(lambda x: x + '0', DP[0][1])) + list(map(lambda x: x + '0', DP[0][0]))
        DP[0][0] = []
        DP[1][0] = list(map(lambda x: x + '1', DP[0][1]))
        DP[0][1] = []
        if sN <= len(DP[1][0]) + len(DP[1][1]):
            r = DP[1][1] + DP[1][0]
            print(r[sN-1])
            break
        sN -= len(DP[1][0]) + len(DP[1][1])
        DP[0], DP[1] = DP[1], [[], []]


else:
    print(1)
