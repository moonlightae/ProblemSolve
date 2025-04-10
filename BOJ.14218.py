from collections import deque

def bfs(l, n):
    v = [-1] * n
    q = deque([(0, 0)])
    while len(q) > 0:
        x, d = q.popleft()
        if d < v[x] or v[x] == -1:
            v[x] = d
            for i in range(len(l[x])):
                q.append((l[x][i], d + 1))
    return v


N, M = map(int, input().split())
L = [[] for i in range(N)]
for i in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    L[a].append(b)
    L[b].append(a)

for i in range(int(input())):
    Lc = L.copy()
    a, b = map(lambda x: x-1, map(int, input().split()))
    Lc[a].append(b)
    Lc[b].append(a)
    print(*bfs(Lc, N))