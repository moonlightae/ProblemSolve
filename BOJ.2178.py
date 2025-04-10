from collections import deque

N, M = map(int, input().split())
l = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
q = deque([(0, 0, 1)])
l[0][0] = 0
t = 0
while len(q) > 0:
    x, y, t = q.popleft()
    if x == N - 1 and y == M - 1:
        break
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M and l[x + dx[i]][y + dy[i]] == 1:
            q.append((x + dx[i], y + dy[i], t + 1))
            l[x+dx[i]][y+dy[i]] = 0

print(t)