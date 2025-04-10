L = []
while True:
    try:
        L.append(int(input()))
    except ValueError or EOFError:
        break
N = max(L)

DP = [1]
K = [1]
k = 0
i = 0
ia = 2
while k < N:
    k += 1
    i += 1
    K.append(0)
    K[k] = 2**(ia-1)
    if i == ia:
        ia += 1
        i = 0
for i in range(1, N):
    DP.append(0)
    DP[i] = K[i] + DP[i-1]

for i in range(len(L)):
    print(f'Case {i+1}: {DP[L[i]-1]}')