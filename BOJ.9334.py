K = int(input())

L = list(map(int, input().split()))
R = [L]
for i in range(K):
    nR = [[] for _ in range(2**(i+1))]
    for j in range(len(R)):
        print(R[j].pop(len(R[j])//2), end=' ')
        if len(R[j]) != 0:
            nR[2 * j] = R[j][:len(R[j])//2]
            nR[2 * j + 1] = R[j][len(R[j])//2:]
    R = nR.copy()
    print('')
