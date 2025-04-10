def times(L):
    r = 1
    for j in L:
        r *= j
    return r

T = int(input())
for _ in range(T):
    N = int(input())
    c = dict()
    for i in range(N):
        n, t = input().split()
        if t in c.keys():
            c[t] += 1
        else:
            c[t] = 1
    l = list(map(lambda x: x + 1, c.values()))
    print(times(l)-1)