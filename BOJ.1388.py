N, M = map(int, input().split())
m = ['' for i in range(N)]
for i in range(N):
    m[i] = input()
i, j = 0, 0
c = 0
while i < N:
    while j < M:
        if m[i][j] == '-':
            c += 1
            while j < M and m[i][j] == '-':
                m[i] = m[i][:j] + '0' + m[i][j+1:]
                j += 1
        else:
            j += 1
    i += 1
    j = 0

i, j = 0, 0
while j < M:
    while i < N:
        if m[i][j] == '|':
            c += 1
            while i < N and m[i][j] == '|':
                m[i] = m[i][:j] + '0' + m[i][j+1:]
                i += 1
        else:
            i += 1
    j += 1
    i = 0

print(c)
