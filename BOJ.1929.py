import math
m, n = map(int, input().split())

L = [1 for i in range(0, n+1)]
L[0] = 0
L[1] = 0
for i in range(2, int(math.sqrt(n)) + 1):
    if L[i] == 1:
        j = 2
        while i * j <= n:
            L[i * j] = 0
            j += 1

for i in range(m, n+1):
    if L[i] == 1:
        print(i)