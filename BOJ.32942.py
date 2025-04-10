A, B, C = map(int, input().split())
f = [[] for i in range(11)]
for x in range(1, 11):
    if B != 0:
        a = (C - A * x) / B
        if int(a) == a and 1 <= a <= 10:
            f[x].append(int(a))
    else:
        a = C / A
        if int(a) == a and 1 <= a <= 10:
            f[int(a)].append(x)


for i in range(10):
    if len(f[i + 1]) == 0:
        print(0)
    else:
        print(*f[i + 1])
