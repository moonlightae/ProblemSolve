N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if ((bool(L[j][i]) and bool(L[i][k])) == True) and L[j][k] == 0:
                L[j][k] = 1

for i in range(N):
    print(*L[i])