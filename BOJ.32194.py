N = int(input())
l = [0] * (N + 2)
l[1] = 1

for i in range(1, N+1):
    c, a, b = map(int, input().split())
    if c == 1:
        if l[b] - l[a-1] == b - a + 1:
            print("Yes")
            l[i+1] = l[i] + 1
        else:
            print("No")
            l[i+1] = l[i]
    else:
        if l[b] - l[a-1] == 0:
            print('Yes')
            l[i+1] = l[i] + 1
        else:
            print('No')
            l[i+1] = l[i]
