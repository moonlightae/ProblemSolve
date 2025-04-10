T = int(input())
k = list()
n = list()
for i in range(T):
    k.append(int(input()))
    n.append(int(input()))

DP = [[] for i in range(max(k) + 1)]
DP[0] = [i for i in range(1, max(n)+1)]
for i in range(1, max(k) + 1):
    for j in range(max(n)):
        DP[i].append(0)
        DP[i][j] = sum(DP[i-1][0:j+1])
for i in range(T):
    print(DP[k[i]][n[i]-1])