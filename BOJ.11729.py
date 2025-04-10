N = int(input())

hmt = [1]
for i in range(1, N):
    hmt.append(0)
    hmt[-1] = hmt[-2] * 2 + 1


def hanoi_tower(n, source, target, auxiliary):
    if n == 1:
        print(source, target)
    else:
        hanoi_tower(n-1, source, auxiliary, target)
        print(source, target)
        hanoi_tower(n-1, auxiliary, target, source)


print(hmt[-1])
if N <= 20:
    hanoi_tower(N, 1, 3, 2)