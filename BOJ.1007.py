for _ in range(int(input())):
    N = int(input())
    L = [[] for __ in range(N)]
    for i in range(N):
        L[i] = list(map(int, input().split()))

    l = []
    for i in range(N):
        for j in range(i+1, N):
            l.append((L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2)
