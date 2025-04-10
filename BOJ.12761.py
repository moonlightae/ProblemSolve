from collections import deque
A, B, N, M = map(int, input().split())
L = [100001] * 100001

q = deque([(N, 0)])
md = 100001
dx = [A, B, 1]
L[N] = 0
while len(q) > 0:
    n, d = q.popleft()
    if n == M:
        md = min(md, d)
    else:
        for i in range(3):
            if 0 <= n + dx[i] < 100001 and d+1 < L[n + dx[i]]:
                L[n + dx[i]] = d+1
                q.append((n+dx[i], d+1))

            if 0 <= n - dx[i] < 100001 and d+1 < L[n - dx[i]]:
                L[n - dx[i]] = d+1
                q.append((n-dx[i], d+1))

            if 0 <= n * dx[i] < 100001 and d+1 < L[n * dx[i]]:
                L[n * dx[i]] = d+1
                q.append((n*dx[i], d+1))

print(md)