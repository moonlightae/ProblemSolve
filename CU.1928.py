N = int(input())

def woobak(n):
    if n == 1:
        print(n)
        return
    elif n % 2 == 0:
        print(n)
        return woobak(n//2)
    else:
        print(n)
        return woobak(3 * n + 1)

woobak(N)