k, a  = 49, 2

DP = [0] * (k)
DP[0] = a
DP[1] = a
for i in range(2, (k)):
    DP[i] = DP[i-1] + DP[i-2]
    if DP[i] >= 30:
        DP[i] = 1

print(DP[-1])