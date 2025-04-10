import sys as s
import collections as c

N = int(input())

L = [[] for _ in range(N)]
for i in range(N):
    L[i] = list(map(int, s.stdin.readline().split()))

x = 0
y = 0
t = L[y][x]
Q = c.deque([(x, y)])
while t != -1:
    if t != 0:
        if y+t < N:
            Q.append((x, y+t))
        if x+t < N:
            Q.append((x+t, y))

    if len(Q) <= 1:
        print("Hing")
        break
    else:
        Q.popleft()
        x = Q[0][0]
        y = Q[0][1]
        t = L[y][x]
    if t == -1:
        print("HaruHaru")
        break