from collections import deque

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
o = 0
for i in range(N):
    for j in range(M):
        if L[i][j] == 1:
            o += 1

l = [[0] * M for _ in range(N)]
b = deque([])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
t = 0
while True:
    po = o
    b.append((0, 0))
    l = [[0] * M for _ in range(N)]
    while len(b) > 0:
        x, y = b.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if L[x + dx[i]][y + dy[i]] == 0 and l[x + dx[i]][y + dy[i]] == 0:
                    b.append((x + dx[i], y + dy[i]))
                    l[x + dx[i]][y + dy[i]] = -1
                elif L[x + dx[i]][y + dy[i]] == 1:
                    o -= 1
                    L[x + dx[i]][y + dy[i]] = 0
                    l[x + dx[i]][y + dy[i]] = -1

    if o == 0:
        break
    else:
        t += 1
        continue
print(t+1)
print(po)