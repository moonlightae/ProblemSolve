# DP 연습
BASIC = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
N = int(input())
for j in range(N-1):
    BASIC.append(list())
    BASIC[-1].append(BASIC[-2][1])
    for i in range(8):
        BASIC[-1].append(BASIC[-2][i] + BASIC[-2][i+2])
    BASIC[-1].append(BASIC[-2][-2])
print(sum(BASIC[-1]) % 1000000000)