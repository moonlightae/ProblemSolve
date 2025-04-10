T = int(input())


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


for _ in range(T):
    L = list(map(int, input().split()))
    if L[0] == L[3] and L[1] == L[4] and L[2] == L[5]:
        if L[2] == 0:
            print(1)
        else:
            print(-1)
    elif L[0] == L[3] and L[1] == L[4]:
        print(0)
    else:
        d = distance(L[0], L[1], L[3], L[4])
        if d == (L[2] + L[5])**2:
            print(1)
        elif d > (L[2] + L[5])**2:
            print(0)
        else:
            s = L[5] if L[2] > L[5] else L[2]
            if d ** (1/2) + s < L[2] + L[5] - s:
                print(0)
            elif d ** (1/2) + s == L[2] + L[5] - s:
                print(1)
            else:
                print(2)
