N, M = map(int, input().split())
l = [[] for i in range(N)]
for i in range(N):
    l[i] = list(map(int, input().split()))
m = 0
for i in range(N-1):
    for j in range(M-1):
        m = max(l[i][j] + l[i+1][j] + l[i][j+1] + l[i+1][j+1], m)

for i in range(N):
    for j in range(M-3):
        m = max(l[i][j] + l[i][j+1] + l[i][j+2] + l[i][j+3], m)

for i in range(N-3):
    for j in range(M):
        m = max(l[i][j] + l[i+1][j] + l[i+2][j] + l[i+3][j], m)

for i in range(N-1):
    for j in range(M-2):
        m = max(l[i][j] + l[i][j+1] + l[i][j+2] + l[i+1][j], m)
        m = max(l[i][j] + l[i][j+1] + l[i][j+2] + l[i+1][j+2], m)
        m = max(l[i][j] + l[i+1][j] + l[i+1][j+1] + l[i+1][j+2], m)
        m = max(l[i+1][j] + l[i+1][j+1] + l[i+1][j+2] + l[i][j+2], m)
        m = max(l[i][j] + l[i][j+1] + l[i][j+2] + l[i+1][j+1], m)
        m = max(l[i][j+1] + l[i+1][j] + l[i+1][j+1] + l[i+1][j+2], m)
        m = max(l[i][j] + l[i][j+1] + l[i+1][j+1] + l[i+1][j+2], m)
        m = max(l[i+1][j] + l[i+1][j+1] + l[i][j+1] + l[i][j+2], m)

for i in range(N-2):
    for j in range(M-1):
        m = max(l[i][j] + l[i+1][j] + l[i+2][j] + l[i][j+1], m)
        m = max(l[i][j] + l[i+1][j] + l[i+2][j] + l[i+2][j+1], m)
        m = max(l[i][j] + l[i][j+1] + l[i+1][j+1] + l[i+2][j+1], m)
        m = max(l[i][j+1] + l[i+1][j+1] + l[i+2][j+1] + l[i+2][j], m)
        m = max(l[i][j] + l[i+1][j] + l[i+2][j] + l[i+1][j+1], m)
        m = max(l[i+1][j] + l[i][j+1] + l[i+1][j+1] + l[i+2][j+1], m)
        m = max(l[i][j] + l[i+1][j] + l[i+1][j+1] + l[i+2][j+1], m)
        m = max(l[i][j+1] + l[i+1][j+1] + l[i+1][j] + l[i+2][j], m)

print(m)