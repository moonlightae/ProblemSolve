N, T = map(int, input().split())
S = input()
for i in range(T):
    L = input()
    xxx = 0
    for j in S:
        if j in L:
            L = L[L.index(j)+1:]
        else:
            xxx = 1
            break

    if xxx == 1:
        print("false")
    else:
        print("true")