import math
m, n = map(int, input().split())

L = [1 for i in range(0, int(math.sqrt(n+1))+1)]
L[0] = 0
L[1] = 0
for i in range(2, int(math.sqrt(int(math.sqrt(n)) + 1))+1):
    if L[i] == 1:
        j = 2
        while i * j <= int(math.sqrt(n+1)):
            L[i * j] = 0
            j += 1

s = 0
for i in range(L.count(1)):
    main = L.index(1)
    L[main] = 0
    j = 2
    while m < main ** j < n:
        s += 1
        j += 1

print(s)