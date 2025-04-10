N = int(input())
L = list(map(int, input().split()))
r = [0] * N
for i in range(N):
    s = []
    mm = 1000000001
    mM = -1000000001
    for j in range(1, N):
        if i >= j:
            main = (L[i] - L[i-j])/j
            if main < mm:
                s.append(main)
                mm = main
        else:
            main = (L[i] - L[j])/(i-j)
            if main > mM:
                s.append(main)
                mM = main
    r[i] = len(s)
print(max(r))