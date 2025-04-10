n, k = map(int, input().split())

s = set()
l = list(map(int, input().split()))
for i in range(k):
    s.add(l[i])
l = list(map(int, input().split()))
for i in range(k):
    s.add(l[i])

if len(s) == n:
    print("YES")
else:
    print("NO")
