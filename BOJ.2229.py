import time as t
import sys as s

N = int(s.stdin.readline())
L = list(map(int, s.stdin.readline().split()))

DP = [0] * N
for i in range(1, N):
    main = L[:i+1]
    M = 0
    m = 0
    for j in range(i):
        r = main[-j:]
        if len(r) == 1 and r != main:
            M = r[0]
            m = r[0]
        elif len(r) > 1 and r != main:
            if r[-j] > M:
                M = r[-j]
            if r[-j] < m:
                m = r[-j]
        else:
            r.sort()
            M = r[-1]
            m = r[0]
        a = DP[i-j] + M - m
        b = DP[i]
        DP[i] = a if a > b else b

print(DP[-1])

# DP = [0] * N
# for i in range(1, N):
#     main = L[:i+1]
#     print(i, main, end=' ')
#     for j in range(i):
#         r = main[-j:]
#         r.sort()
#         print((r[-1], r[0]), end=' ')
#         a = DP[i-j] + r[-1] - r[0]
#         b = DP[i]
#         DP[i] = a if a > b else b
#     print()
#
# print(DP)
