import sys as s
import time as t

t0 = t.time()
n = int(s.stdin.readline())
while n > 0:
    n -= 1
    i = int(s.stdin.readline())
    ii = i
    if i == 0:
        zn = 1
        on = 0
    if i == 1:
        zn = 0
        on = 1
    else:
        an = 1
        anpo = 0
        while ii > 0:
            ii -= 1
            an += anpo
            an, anpo = anpo, an
        zn = an
        an = 0
        anpo = 1
        while i > 0:
            i -= 1
            an += anpo
            an, anpo = anpo, an
        on = an
    print(zn, on)

t1 = t.time()
print(t1-t0)