from collections import deque

N, M, K = map(int, input().split())
L = [[[] for i in range(M)] for j in range(K)]

for i in range(K):
    for j in range(M):
        L[i][j] = list(map(int, input().split()))

z = 0
q = deque()
d = 0
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for k in range(K):
    for i in range(M):
        for j in range(N):
            if L[k][i][j] == 0:
                z += 1
            elif L[k][i][j] == 1:
                q.append((i, j, k, d))

while len(q) > 0:
    mx, my, mz, d = q.popleft()
    for i in range(6):
        X = dx[i]
        Y = dy[i]
        Z = dz[i]
        if 0 <= mx + X < M and 0 <= my + Y < N and 0 <= mz + Z < K and L[mz + Z][mx + X][my + Y] == 0:
            q.append((mx + X, my + Y, mz + Z, d + 1))
            L[mz + Z][mx + X][my + Y] = 1
            z -= 1

if z == 0:
    print(d)
else:
    print(-1)