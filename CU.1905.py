import sys as s
s.setrecursionlimit(100000000)

a = int(input())

def alpha(a):
    if a == 1:
        return 1
    else:
        return alpha(a-1) + a


print(alpha(a))