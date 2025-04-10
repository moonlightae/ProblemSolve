import sys as s

N = int(s.stdin.readline())
stack = list()
for i in range(N):
    command = s.stdin.readline()
    if 'pu' in command:
        c, integer = command.split()
        stack.append(integer)
    elif 'po' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'si' in command:
        print(len(stack))
    elif 'em' in command:
        print(0 if len(stack) != 0 else 1)
    elif 'to' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
