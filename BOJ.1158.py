N, K = map(int, input().split())
A = [i for i in range(1, N+1)]
out = []

for i in range(0, N):
    x = (K-1) % len(A)
    out.append(A.pop(x))
    if len(A) != 0:
        A = A[x:] + A[:x]

print('<' + str(out)[1:-1] + '>')