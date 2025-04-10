import sys as s
def add(L, a):
    i = len(L)
    L.append(a)
    while i > 0:
        pi = (i - 1) // 2
        if L[pi] < L[i]:
            L[pi], L[i] = L[i], L[pi]
            i = pi
        else:
            break
    return L

def p(L):
    l = len(L)
    if l == 0:
        print(0)
        return L
    elif l == 1:
        print(L[0])
        L.pop()
        return L
    else:
        print(L[0])
        L[0] = L.pop()
        l -= 1
        i = 0
        while True:
            if i * 2 + 2 < l:
                li = i * 2 + 1
                ri = i * 2 + 2
                m = L[li] if L[li] > L[ri] else L[ri]

                if L[i] < m == L[li]:
                    L[i], L[li] = L[li], L[i]
                    i = li
                elif L[i] < m == L[ri]:
                    L[i], L[ri] = L[ri], L[i]
                    i = ri
                else:
                    break
            elif i * 2 + 1 < l:
                n = L[i * 2 + 1]
                if n > L[i]:
                    L[i], L[i * 2 + 1] = L[i * 2 + 1], L[i]
                    break
                else:
                    break
            else:
                break
    return L

L = []

N = int(input())
for _ in range(N):
    R = int(s.stdin.readline())
    if R == 0:
        L = p(L)
    else:
        L = add(L, R)