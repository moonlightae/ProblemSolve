A, B = map(int, input().split())
N = int(input())
l = []
for i in range(N):
    l.append(int(input()))
r = []
for i in range(N+1):
    if i != N:
        r.append(l[i]-B + 1 if l[i] > B else B-l[i] + 1)
    else:
        r.append(A-B if A > B else B-A)

print(min(r))