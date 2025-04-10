N = int(input())
S = [_**2 for _ in range(1, 225)]
L = [4] * (N+1)
L[1] = 1
k = 0
if N in S:
    print(1)
else:
    for i in range(1, N+1):
        for j in S:
            if i == S[k]:
                L[i] = 1
                k += 1
            elif i - j > 0:
                if L[i-j] + 1 < L[i]:
                    L[i] = L[i-j] + 1
            else:
                break

    print(L[N])