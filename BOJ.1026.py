N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort(reverse=True)

s = 0
for i in range(N):
    s += A[i] * B[i]

print(s)