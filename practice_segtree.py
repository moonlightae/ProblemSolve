import sys as s
def se(s, e, n):
    global l, L
    if s == e:
        l[n] = L[s]
    else:
        m = (s+e)//2
        l[n] = se(s, m, n*2) + se(m+1, e, n*2 + 1)
    return l[n]

def su(s, e, n, a, b):
    global l
    if a > e or b < s:
        return 0
    elif a <= s and b >= e:
        return l[n]
    else:
        m = (s+e)//2
        return su(s, m, n * 2, a, b) + su(m+1, e, n * 2 + 1, a, b)

def ch(s, e, n, w, r):
    global l
    if s <= r <= e:
        l[n] += w
        if s == e:
            return
        else:
            mid = (s+e)//2
            ch(s, mid, n * 2, w, r)
            ch(mid + 1, e, n * 2 + 1, w, r)
            return
    else:
        return

N, M, K = map(int, input().split())
L = [0] * N
for i in range(N):
    L[i] = int(s.stdin.readline())
S = 4 * N + 1

l = [0] * S
se(0, N-1, 1)

for i in range(K + M):
    print(l)
    print(L)
    a, b, c = map(int, s.stdin.readline().split())
    if a == 1:
        ch(0, N-1, 1, c-L[b-1], b-1)
        L[b-1] = c
    else:
        s.stdout.write(f"{su(0, N-1, 1, b-1, c)}\n")