N = int(input())
L = [tuple(map(int, input().split())) for _ in range(N)]

L.sort(key=lambda x: (x[1], x[0]))

e = 0
r = 0
while len(L) > 0:
    m = L.pop(0)
    if m[0] >= e:
        e = m[1]
        r += 1

print(r)