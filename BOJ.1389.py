from collections import deque

def bfs(a, b, l):
    global N
    v = [False] * N
    v[a] = True
    q = deque([(a, 0)])
    while len(q) > 0:
        x, t = q.popleft()
        if x == b:
            return t
        for y in l[x]:
            if not v[y]:
                q.append((y, t + 1))
                v[y] = True
    return None



N, M = map(int, input().split())
L = [[] for _ in range(N)]
for i in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    L[a].append(b)
    L[b].append(a)

K = [0] * N
for i in range(N):
    for j in range(N):
        k = bfs(i, j, L)
        K[i] += k

print(K.index(min(K))+1)