m, M = map(int, input().split())
s = M - m + 1
l = [1] * s

x = 2
while (x ** 2) <= M:
    alpha = ((m // (x ** 2)) + 1) * (x ** 2) - m
    while alpha <= M - m:
        l[alpha] = 0
        alpha += x ** 2
    x += 1

print(sum(l))