# 2차원 배열로 받고, 배열을 실제로 4개로 쪼개자
def pp(l):
    for i in range(len(l)):
        print(*l[i])

def su(l, s):
    r = 0
    for i in range(s):
        r += sum(l[i])
    return r

def cu(l, s):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for i in range(s//2):
        l1.append(l[i][:s//2])
        l2.append(l[i][s//2:])
    for i in range(s//2, s):
        l3.append(l[i][:s//2])
        l4.append(l[i][s//2:])
    return l1, l2, l3, l4


def co(l, s):
    global c1, c2
    ss = su(l, s)
    if ss == 0:
        c1 += 1
        return 1
    elif ss == s ** 2:
        c2 += 1
        return 1
    else:
        l1, l2, l3, l4 = cu(l, s)
        return co(l1, s//2) + co(l2, s//2) + co(l3, s//2) + co(l4, s//2)

S = int(input())
L = [list(map(int, input().split())) for _ in range(S)]

c1 = 0
c2 = 0

co(L, S)
print(c1)
print(c2)