from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
L = [[] for i in range(M)]

for i in range(M):
    L[i] = list(map(int, input().split()))

z = 0
q = deque()
d = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(M):
    for j in range(N):
        if L[i][j] == 0:
            z += 1
        elif L[i][j] == 1:
            q.append((i, j, d))

while len(q) > 0:
    mx, my, d = q.popleft()
    for i in range(4):
        X = dx[i]
        Y = dy[i]
        if 0 <= mx + X < M and 0 <= my + Y < N and L[mx + X][my + Y] == 0:
            q.append((mx + X, my + Y, d + 1))
            L[mx + X][my + Y] = 1
            z -= 1

if z == 0:
    print(d)
else:
    print(-1)