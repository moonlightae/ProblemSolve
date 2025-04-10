import math as m
def turn(l, t):  # t가 가장 왼쪽에 오도록 트리의 형태를 유지하면서 돌려주는 함수
    if len(l) == 1:
        return l
    else:
        size = len(l)
        if l.index(t) >= size//2:
            l.reverse()
        return turn(l[:size//2], t) + l[size//2:]

N = int(input())
L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

a = 2 ** (N-1)  # N번 줄 원소의 개수

R1 = [[0] * a for _ in range(a)]
R2 = [[0] * a for _ in range(a)]

for i in range(a):
    main1 = turn(L1, i + 1)
    main2 = turn(L2, i + 1)
    for j in range(a):
        b = 2 * m.ceil(m.log(j + 1, 2))
        R1[i][main1[j]-1] = b
        R2[i][main2[j]-1] = b

print(R1)
print(R2)