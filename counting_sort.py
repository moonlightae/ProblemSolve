import sys as s

N = int(input())
L = list()
for i in range(N):
    L.append(int(s.stdin.readline()))

B = list()
for i in range(max(L) + 1):
    B.append(L.count(i) + (B[i-1] if i > 1 else 0))

C = [0 for i in range(len(L))]
for i in range(len(L)):
    B[L[-i-1]] -= 1
    C[B[L[-i-1]]] = L[-i-1]
    print(*C)