T = int(input())
DP = [1, 2, 4]
N = []
for i in range(T):
    N.append(int(input()))

for i in range(3, max(N)):
    DP.append(0)
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

for i in range(T):
    print(DP[N[i]-1])