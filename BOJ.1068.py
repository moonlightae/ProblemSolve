N = int(input())
L = list(map(int, input().split()))
s = int(input())
R = 0

M = [[] for i in range(N)]
for i in range(N):
    if L[i] == -1:
        R = i
    else:
        M[L[i]].append(i)

if R == s:
    print(0)
else:
    q = [s]
    if L[s] != -1:
        M[L[s]].remove(s)
    while len(q) > 0:
        t = q.pop(0)
        for i in range(len(M[t])):
            q.append(M[t].pop())

    x = 0
    q = [R]
    while len(q) > 0:
        t = q.pop(0)
        if len(M[t]) == 0:
            x += 1
        else:
            for i in range(len(M[t])):
                q.append(M[t][i])

    print(x)