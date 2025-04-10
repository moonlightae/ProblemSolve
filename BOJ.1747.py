def pal(n):
    if len(n) == 1 or len(n) == 0:
        return True
    if n[0] == n[-1]:
        return pal(n[1:-1])
    else:
        return False

N = int(input())
l = [1] * 1003002
l[0] = 0
l[1] = 0
m = 2
while m < 1002:
    i = m**2
    while i < 1003002:
        l[i] = 0
        i += m
    m += 1
    while l[m] == 0:
        m += 1

r = []
for i in range(1003002):
    if pal(str(i)) and l[i] == 1 and N <= i:
        print(i)
        break