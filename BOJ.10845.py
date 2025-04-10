queue = []
import sys as s

N = int(input())
for i in range(N):
    command = s.stdin.readline()
    if command[0:2] == 'pu':
        a, b = command.split()
        queue.append(b)
    elif command[0:2] == 'po':
        if len(queue) > 0:
            s.stdout.write(f'{queue.pop(0)}\n')
        else:
            s.stdout.write('-1\n')
    elif command[0:2] == 'si':
        s.stdout.write(f'{len(queue)}\n')
    elif command[0:2] == 'em':
        if len(queue) > 0:
            s.stdout.write('0\n')
        else:
            s.stdout.write('1\n')
    elif command[0:2] == 'fr':
        if len(queue) > 0:
            s.stdout.write(f'{queue[0]}\n')
        else:
            s.stdout.write('-1\n')
    else:
        if len(queue) > 0:
            s.stdout.write(f'{queue[-1]}\n')
        else:
            s.stdout.write('-1\n')