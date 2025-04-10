T = int(input())
L = [0] * T
for i in range(T):
    L[i] = int(input())

M = max(L)
DP = [1] * (M + 1)
DP[0] = 0
for i in range(2, M + 1):
    j = i
    while j < M + 1:
        DP[j] += i
        j += i

r = [0] * (M + 1)
for i in range(1, M + 1):
    r[i] = DP[i] + r[i-1]

for i in range(T):
    print(r[L[i]])