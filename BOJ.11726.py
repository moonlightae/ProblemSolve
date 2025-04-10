DP = [1, 2]
N = int(input())

for i in range(2, N):
    DP.append(0)
    DP[i] = (DP[i-1] + DP[i-2]) % 10007

print(DP[N-1])