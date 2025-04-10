N = int(input())

for i in range(N):
    L = list(map(int, input().split()))
    L.pop(0)
    S = sum(L) / len(L)
    n = 0
    for j in range(len(L)):
        if S < L[j]:
            n += 1
    print(f"{round(n * 100 / len(L), 3)}%")
