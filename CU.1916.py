# 여기에 코드를 작성하시오.
N = int(input())
L = [0] * N

def fibo(n):
    global L
    if n == 0 or n == 1:
        return 1
    if L[n] != 0:
        return L[n]
    else:
        L[n] =  (fibo(n-1) + fibo(n-2)) % 10009

    return L[n]

print(fibo(N-1))
