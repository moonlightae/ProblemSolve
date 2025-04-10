N = int(input())
L = [list(map(int, input().split())) * N for _ in range(N)]
v = [[False] * N for _ in range(N)]
c = 0
q = [(0, 0)]
while len(q) > 0:
    x, y = q.pop()
    t = L[x][y]
    v[x][y] = True
    if t == -1:
        c = 1
        break
    if t != 0 and x + t < N and not v[x + t][y]:
        q.append((x + t, y))
    if t != 0 and y + t < N and not v[x][y + t]:
        q.append((x, y + t))

print("HaruHaru" if c == 1 else "Hing")