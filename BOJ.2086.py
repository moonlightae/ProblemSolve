a, b = map(int, input().split())
DP = [1, 1]
s = 0
for i in range(2, b):
    DP.append(0)
    DP[-1] = DP[-2] + DP[-3]
    if i >= a-1:
        s += DP[-1]
    DP = DP[-2:]

print(s)
