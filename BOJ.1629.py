def func(a, b, c):
    if b == 1:
        return a % c
    else:
        alpha = func(a, b // 2, c) % c
        if b % 2 == 0:
            return (alpha * alpha) % c
        else:
            return (alpha * alpha * a) % c


x, y, z = map(int, input().split())
print(func(x, y, z))
