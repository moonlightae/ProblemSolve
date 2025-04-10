N = int(input())

def woobak(n):
    if n == 1:
        print(n)
    elif n % 2 == 0:
        woobak(n//2)
        print(n)
    else:
        woobak(3 * n + 1)
        print(n)

woobak(N)