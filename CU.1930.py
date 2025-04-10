L = []

while True:
    L.append(list(map(int, input().split())))
    if L[-1] == [0, 0]:
        L.remove([0,0])
        break

Lk = []
Ln = []
for i in range(len(L)):
    Lk.append(L[i][0])
    Ln.append(L[i][1])

DP = [[i for i in range(max(Ln)+1)] for i in range(max(Lk)+1)]

for i in range(1, max(Lk)+1):
    for j in range(1, max(Ln)+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j]

for i in range(len(L)):
    print(DP[Lk[i]][Ln[i]])
