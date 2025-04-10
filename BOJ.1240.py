from collections import deque

N, M = map(int, input().split())
l = [[] for _ in range(N)]

for _ in range(N-1):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    l[x].append((y, d))
    l[y].append((x, d))

for i in range(M):
    x, y = map(lambda a: a-1, map(int, input().split()))
    v = [False] * N
    v[x] = True
    q = deque([(x, 0)])
    md = 1000001
    while len(q) > 0:
        z, d = q.popleft()
        if z == y:
            md = md if md < d else d
        else:
            for j in range(len(l[z])):
                if not v[l[z][j][0]]:
                    q.append((l[z][j][0], d + l[z][j][1]))
                    v[l[z][j][0]] = True
    print(md)
