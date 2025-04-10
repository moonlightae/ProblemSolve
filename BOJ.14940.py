from collections import deque

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
l = [[0] * M for _ in range(N)]

def f():
    global M, N, L
    for i in range(N):
        for j in range(M):
            if L[i][j] == 2:
                return i, j

x, y = f()
q = deque([])
q.append((x, y, 0))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while len(q) > 0:
    mx, my, d = q.popleft()
    if d == 0:
        l[mx][my] = -2
    else:
        l[mx][my] = d
    for i in range(4):
        if 0 <= mx + dx[i] < N and 0 <= my + dy[i] < M and L[mx + dx[i]][my + dy[i]] == 1:
            q.append((mx + dx[i], my + dy[i], d + 1))
            L[mx + dx[i]][my + dy[i]] = -1

for i in range(N):
    for j in range(M):
        if l[i][j] == 0 and L[i][j] == 1:
            l[i][j] = -1

l[x][y] = 0

for i in range(N):
    print(*l[i])
