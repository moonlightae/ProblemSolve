N = int(input())
l = list(map(int, input().split()))
p = []
for i in l:
    j = 1
    while True:
        j += 1
        if i == 1:
            break
        if i == 2:
            p.append(i)
            break
        if i % j == 0:
            break
        if j ** 2 > i:
            p.append(i)
            break
print(len(p))