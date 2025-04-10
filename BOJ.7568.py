T = int(input())
L = list()
P = [1 for i in range(T)]
for i in range(T):
    L.append(tuple(map(int, input().split())))

for i in range(T):
    Ls = L.copy()
    Ls.pop(i)
    for j in range(T-1):
        if L[i][0] < Ls[j][0] and L[i][1] < Ls[j][1]:
            P[i] += 1
for i in range(T):
    print(P[i], end=' ')
