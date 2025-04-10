a, b = map(int, input().split())

def alpha(x, y):
    if x % 2 == 1:
        print(x, end=' ')
    if x == y:
        return
    x += 1
    alpha(x, y)


alpha(a, b)