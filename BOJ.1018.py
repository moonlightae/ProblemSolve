N, M = map(int, input().split())
Chess = [[0 for i in range(M)] for _ in range(N)]
Pan = []

for i in range(N):
    L = input()
    for j in range(M):
        Chess[i][j] = L[j]
        if (i + j) % 2 == 0:
            if Chess[i][j] == 'W':
                Chess[i][j] = 1
            else:
                Chess[i][j] = 0
        else:
            if Chess[i][j] == 'B':
                Chess[i][j] = 1
            else:
                Chess[i][j] = 0

Pan_Size = 7
for i in range(N-Pan_Size):
    for j in range(M-Pan_Size):
        alpha = Chess[i:i+8]
        beta = []
        for k in range(8):
            beta.append(alpha[k][j:j+8])
        gamma = 0
        for k in range(8):
            gamma += sum(beta[k])
        Pan.append(gamma)
if 64 - max(Pan) > min(Pan):
    print(min(Pan))
else:
    print(64 - max(Pan))