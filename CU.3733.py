a, b = map(int, input().split())
N = b
DP = [1]

for i in range(1, N+1):
    k = i
    DP.append(0)
    while True:
        if k == 1:
            DP[i] += 1
            break
        else:
            if len(DP) > k and DP[k] != 0:
                DP[i] += DP[k]
                break
            if k % 2 == 0:
                k //= 2
                DP[i] += 1
            else:
                k = (3 * k + 1)//2
                DP[i] += 2

R = DP[a:b+1]
print(R.index(max(R)) + a, max(R))