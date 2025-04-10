N, K = map(int, input().split())

out = []
m = 0
def h(n, s, t, a):
    global out, m
    if n == 1:
        if m == K-1:
            out = [s, t]
        m += 1
    else:
        h(n-1, s, a, t)
        if m == K-1:
            out = [s, t]
        m += 1
        h(n-1, a, t, s)


h(N, 1, 3, 2)
print(*out)