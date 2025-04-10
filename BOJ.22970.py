input()
N=list(map(int, input().split()))
p = [0, len(N)]
r = []

for i in range(1, len(N)-1):
    if (N[i-1] > N[i] and N[i] < N[i+1]) or N[i-1] == N[i] or N[i+1] == N[i]:
        p.append(i)

p.sort()
for i in range(len(p) - 1):
    r.append(len(N[p[i]:p[i + 1] + 1]) if max(N[p[i]:p[i + 1] + 1]) != min(N[p[i]:p[i + 1] + 1]) else 1)

print(max(r))
