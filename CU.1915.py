import sys as s
s.setrecursionlimit(100000000)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2)) % 10009


print(fibo(int(input())))