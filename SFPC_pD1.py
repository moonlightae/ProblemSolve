a = list(map(int, input().split()))

b = list(map(int, input().split()))
c = list(map(int, input().split()))

s1 = 1000001
for i in range(4):
    m = b[i]//a[i]
    if m < s1:
        s1 = m

c[3] += b[3] - (s1 * a[3])
s2 = 1000001
for i in range(4):
    m = c[i]//a[i]
    if m < s2:
        s2 = m

print(s1+s2)