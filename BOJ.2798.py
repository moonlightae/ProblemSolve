N, A = map(int, input().split())
l = list(map(int, input().split()))
out = list()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            alpha = l[i] + l[j] + l[k]
            if alpha <= A:
                out.append(alpha)

print(max(out))