from collections import deque

N, M = map(int, input().split())
L = [[] for i in range(N)]
v = [False] * N
for i in range(M):
    a, b = map(int, input().split())
    L[a-1].append(b-1)
    L[b-1].append(a-1)

c = 0
while sum(v) < len(v):
    x = v.index(False)
    q = deque([x])
    v[x] = True
    c += 1
    while len(q) > 0:
        m = q.popleft()
        for i in range(len(L[m])):
            if not v[L[m][i]]:
                q.append(L[m][i])
                v[L[m][i]] = True

print(c)
