K, N = map(int, input().split())
l = [0] * K
for i in range(K):
    l[i] = int(input())

def length(a):
    s = 0
    for j in range(K):
        s += l[j] // a
    if s >= N:
        return True
    else:
        return False

right = max(l)
left = 1
while right >= left:
    mid = (left + right)//2
    alpha = length(mid)
    if alpha:
        r = 0
        left = mid + 1
    else:
        r = 1
        right = mid - 1

print(mid - r)