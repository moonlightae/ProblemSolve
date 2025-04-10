import sys as s

N = int(input())
L = [0 for i in range(10001)]
for i in range(N):
    L[int(s.stdin.readline())] += 1

for i in range(10001):
    for j in range(L[i]):
        print(i)