alpha = 1000000007


def func(a, b):
    if b == 0:
        return 1
    x = func(a, b//2)
    if b % 2 == 0:
        return ((x % alpha) * (x % alpha)) % alpha
    else:
        return ((x % alpha) * (x % alpha) * (a % alpha)) % alpha


A = int(input())
B = int(input())

print(func(A, B))
