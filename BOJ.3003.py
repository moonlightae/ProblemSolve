L = [1, 1, 2, 2, 2, 8]
R = list(map(int, input().split()))

X = list(map(lambda x, y: x - y, L, R))
print(*X)