import sys as s

T = int(input())
D = []

for i in range(T):
    c = s.stdin.readline()[:-1]
    if len(list(c.split())) == 2:
        c, n = c.split()
        n = int(n)
    if c == 'push_front':
        D.insert(0, n)
    elif c == 'push_back':
        D.append(n)
    elif c == 'pop_front':
        if len(D) > 0:
            s.stdout.write(f'{D.pop(0)}\n')
        else:
            s.stdout.write('-1\n')
    elif c == 'pop_back':
        if len(D) > 0:
            s.stdout.write(f'{D.pop()}\n')
        else:
            s.stdout.write('-1\n')
    elif c == 'size':
        s.stdout.write(f'{len(D)}\n')
    elif c == 'empty':
        s.stdout.write(f'{int(len(D) == 0)}\n')
    elif c == 'front':
        if len(D) > 0:
            s.stdout.write(f'{D[0]}\n')
        else:
            s.stdout.write('-1\n')
    elif c == 'back':
        if len(D) > 0:
            s.stdout.write(f'{D[-1]}\n')
        else:
            s.stdout.write('-1\n')
