n, m, k = 10, 9, 19
c = [15, 25, 9, 7, 17,26,32,19,8,31]
s = []
for i in range(n):
    r = c[i]
    while r > 0:
        if r >= m:
            s.append(m)
            r -= m
        else:
            s.append(r)
            r = 0


s.sort(reverse=True)
print(sum(s[:k]))
