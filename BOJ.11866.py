import sys as s
N, K = map(int, input().split())
l = [i + 1 for i in range(N)]
s.stdout.write('<')
alpha = K - 1
for i in range(N):

    main = l.pop(alpha)

    s.stdout.write(f'{main}')
    if i + 1 < N:
        s.stdout.write(', ')
        alpha += K - 1
        alpha %= len(l)

s.stdout.write('>')