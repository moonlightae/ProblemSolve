def union(a, b, L):
    for i in range(len(L)):
        if L[i] == b:
            L[i] = L[a]


n, m = map(int, input().split())

L = [i for i in range(n+1)]

for i in range(m):
    command = tuple(map(int, input().split()))
    if command[0] == 0:
        union(command[1], command[2], L)

    if command[0] == 1:
        print("YES" if L[command[1]] == L[command[2]] else "NO")