from collections import deque

N, M, V = map(int, input().split())
L = [[] for _ in range(N)]
v = [False] * N
for i in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    L[a].append(b)
    L[b].append(a)
for i in range(N):
    L[i].sort()

# DFS
q = [V-1]
while len(q) > 0:
    x = q.pop()
    if not v[x]:
        print(x+1, end=' ')
        v[x] = True
        for i in range(len(L[x])):
            q.append(L[x][-1-i])
print()
# BFS
q = deque([V-1])
v = [False] * N
v[V-1] = True
while len(q) > 0:
    x = q.popleft()
    print(x+1, end=' ')
    for i in range(len(L[x])):
        if not v[L[x][i]]:
            q.append(L[x][i])
            v[L[x][i]] = True

