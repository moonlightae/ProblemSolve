N, M = map(int, input().split())
L = list(map(int, input().split()))

def s(l, h):
    return sum(list(map(lambda x: x - h if  x > h else 0, l)))

l = 0
r = max(L)
while l != r - 1:
    i = (l+r)//2
    if s(L, i) < M:
        r = i
    else:
        l = i

print(l)