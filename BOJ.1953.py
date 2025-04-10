N = int(input())

def aste(n):
    if n != 0:
        aste(n-1)
        print("*" * n)
aste(N)
