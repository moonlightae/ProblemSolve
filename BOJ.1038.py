DP = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], [], [], [], [], [], [], [], [], []]

N = int(input())
r = 0
for i in range(1, 10):
    for j in range(len(DP[i-1])):
        main = DP[i-1][j][0]
        if main == '0':
            DP[i].append('1' + DP[i-1][j])
        if main == '1' or main == '0':
            DP[i].append('2' + DP[i-1][j])
        if main == '2' or main == '1' or main == '0':
            DP[i].append('3' + DP[i-1][j])
        if main == '3' or main == '2' or main == '1' or main == '0':
            DP[i].append('4' + DP[i-1][j])
        if main == '4' or main == '3' or main == '2' or main == '1' or main == '0':
            DP[i].append('5' + DP[i-1][j])
        if main == '5' or main == '4' or main == '3' or main == '2' or main == '1' or main == '0':
            DP[i].append('6' + DP[i-1][j])
        if main == '6' or main == '5' or main == '4' or main == '3' or main == '2' or main == '1' or main == '0':
            DP[i].append('7' + DP[i-1][j])
        if main == '7' or main == '6' or main == '5' or main == '4' or main == '3' or main == '2' or main == '1' or main == '0':
            DP[i].append('8' + DP[i-1][j])
        if main == '8' or main == '7' or main == '6' or main == '5' or main == '4' or main == '3' or main == '2' or main == '1' or main == '0':
            DP[i].append('9' + DP[i-1][j])

    if len(DP[0]) + len(DP[1]) + len(DP[2]) + len(DP[3]) + len(DP[4]) + len(DP[5]) + len(DP[6]) + len(DP[7]) + len(DP[8]) + len(DP[9]) > N:
        r = 1

if r == 1:
    DP = DP[0] + sorted(DP[1]) + sorted(DP[2]) + sorted(DP[3]) + sorted(DP[4]) + sorted(DP[5]) + sorted(DP[6]) + sorted(DP[7]) + sorted(DP[8]) + sorted(DP[9])
    print(DP[N])


else:
    print(-1)