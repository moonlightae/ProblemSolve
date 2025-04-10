n = int(input())
s = list(map(int, input().split()))
s.reverse()
count = 0


def hanoi_count(n, source, aux, target, L, max):
    global count
    R = []
    if len(L) == 1:
        count += 1
    elif len(L) == 0:
        return
    else:
        for i in range(n):
            if L[i] == max:
                count += 1
                max -= 1
            else:
                count += 1
                R.append(L[i])
        R.reverse()
        hanoi_count(len(R), aux, source, target, R, max)

def hanoi(n, source, aux, target, L, max):
    R = []
    if len(L) == 1:
        print(source, target)
    elif len(L) == 0:
        return
    else:
        for i in range(n):
            if L[i] == max:
                print(source, target)
                max -= 1
            else:
                print(source, aux)
                R.append(L[i])
        R.reverse()
        hanoi(len(R), aux, source, target, R, max)


hanoi_count(n, 1, 2, 3, s, n)
print(count)
hanoi(n, 1, 2, 3, s, n)