def func(x):
    if len(D) - 1 > x:
        return D[x]
    alpha = list()
    alpha.append(func(x-1) + 1)
    if x % 3 == 0:
        alpha.append(func(x//3) + 1)
    if x % 2 == 0:
        alpha.append(func(x//2) + 1)
    return min(alpha)


D = [999, 0]
N = int(input())
for i in range(2, N+1):
    D.append(D[i-1] + 1)
    if i % 3 == 0:
        alpha = D[i//3] + 1
        D[i] = D[i] if D[i] <= alpha else alpha
    if i % 2 == 0:
        alpha = D[i//2] + 1
        D[i] = D[i] if D[i] <= alpha else alpha

print(D[N])