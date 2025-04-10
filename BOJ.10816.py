import sys as s
import bisect as b

N = int(s.stdin.readline())
l = list(map(int, s.stdin.readline().split()))
l.sort()
M = int(s.stdin.readline())
r = list(map(int, s.stdin.readline().split()))

for i in range(M):
    main = b.bisect_left(l, r[i])
    if main != -1:
        s.stdout.write(f'{(b.bisect_right(l, r[i]) - main)} ')
    else:
        s.stdout.write('0 ')