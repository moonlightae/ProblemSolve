N = int(input())
L = list(map(int, input().split()))

R = list(set(L))
R.sort()

def f(x, m, M):
    global R
    i = (m+M)//2
    if R[i] == x:
        return i
    elif R[i] < x:
        return f(x, i + 1, M)
    else:
        return f(x, m, i - 1)

l = map(lambda x: f(x, 0, len(R)-1), L)
print(*l)